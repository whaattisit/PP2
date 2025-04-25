import pygame
import random
from data.databaseconnect import connect
import json

conn = connect()
cur = conn.cursor()

# Constants
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
WHITE, GREEN, BLACK, RED, BLUE = (255, 255, 255), (0, 255, 0), (0, 0, 0), (255, 0, 0), (0, 0, 255)

# Display initializing
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 15)
pygame.display.set_caption("Snake")

# user initialize i vse takoye
def get_username(screen, font):
    username = ""
    active = True
    input_box = pygame.Rect(200, 150, 200, 40)

    while active:
        screen.fill(WHITE)
        pygame.draw.rect(screen, BLACK, input_box, 2)

        text_surface = font.render(username, True, BLACK)
        screen.blit(text_surface, (input_box.x + 5, input_box.y + 5))

        prompt = font.render("Write down the name and press Enter:", True, BLACK)
        screen.blit(prompt, (input_box.x, input_box.y - 30))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    active = False
                elif event.key == pygame.K_BACKSPACE:
                    username = username[:-1]
                else:
                    username += event.unicode

    cur.execute("SELECT id FROM game_user WHERE username = %s", (username,))
    row = cur.fetchone()
    if row:
        return row[0]
    cur.execute("INSERT INTO game_user (username) VALUES (%s) RETURNING id", (username,))
    conn.commit()
    id = cur.fetchone()
    return id


def load_user_state(user_id):
    cur.execute("SELECT score, level, state FROM user_score WHERE user_id = %s", (user_id,))
    row = cur.fetchone()
    if row:
        score, level, state = row
        return score, level, state
    return 0, 1, None

# Neccessary parameters
user_id = get_username(screen, font)
score, level, saved_state = load_user_state(user_id)
speed = 15 + (level - 1)

if saved_state:
    snake = saved_state["snake"]
    direction = tuple(saved_state["direction"])
    food = tuple(saved_state["food"])
    food_type = saved_state.get("food_type", "normal")
    food_timer = saved_state.get("food_timer", 0)
else:
    snake = [(100, 100), (90, 100), (80, 100)]
    direction = (CELL_SIZE, 0)
    food = (random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE))
    food_type = "normal"
    food_timer = 0

# Food function (havchik, nyamka, SOTNI NYAMKI)
def spawn_food():
    global food_type, food_timer
    while True:
        new_food = (random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE))
        if new_food not in snake:
            # random chance of temp food
            if random.random() < 0.25:
                food_type = "temp"
                food_timer = pygame.time.get_ticks()
            else:
                food_type = "normal"
                food_timer = 0
            return new_food
        

done = False
while not done:
    screen.fill(WHITE)

    # event queue chota tam :O
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and direction != (0, CELL_SIZE):
                direction = (0, -CELL_SIZE) # if w pressed and snake doesn't look in opposite direction then koroch vi ponyali
            if event.key == pygame.K_s and direction != (0, -CELL_SIZE):
                direction = (0, CELL_SIZE)
            if event.key == pygame.K_a and direction != (CELL_SIZE, 0):
                direction = (-CELL_SIZE, 0)
            if event.key == pygame.K_d and direction != (-CELL_SIZE, 0):
                direction = (CELL_SIZE, 0)
            if event.key == pygame.K_p:
                paused = True
                state = {
                    "snake": snake,
                    "direction": direction,
                    "food": food,
                    "food_type": food_type,
                    "food_timer": food_timer
                }
                state_json = json.dumps(state)
                cur.execute("""
                    INSERT INTO user_score (user_id, score, level, state)
                    VALUES (%s, %s, %s, %s)
                    ON CONFLICT (user_id)
                    DO UPDATE SET score = EXCLUDED.score, level = EXCLUDED.level, state = EXCLUDED.state
                    """, (user_id, score, level, state_json))
                conn.commit()

                while paused:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            paused = False
                    pause_text = font.render("Paused", True, BLACK)
                    screen.blit(pause_text, (WIDTH/2, HEIGHT/2))
                    pygame.display.flip()
                    clock.tick(speed)
                    

    # snake head
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1]) # first tuple first coordinate + direction first coordinate and same for y

    # checking lose conditions 
    if new_head in snake or not (0 <= new_head[0] < WIDTH and 0 <= new_head[1] < HEIGHT):
        done = True
        break

    # move of a snake 
    snake.insert(0, new_head)

    # check if we should delete tail
    if new_head == food:
        score += 1
        if score % 5 == 0:  
            level += 1
            speed += 1
        food = spawn_food()
    else:
        snake.pop()
    
    if food_type == "temp":
        elapsed = pygame.time.get_ticks() - food_timer
        if elapsed > 5000:  # 5 sec ф
            food = spawn_food()
            snake.pop()
    
    # draw of food
    if food_type == "temp":
        pygame.draw.rect(screen, BLUE, (*food, CELL_SIZE, CELL_SIZE))  # blue temporary food
    else:
        pygame.draw.rect(screen, RED, (*food, CELL_SIZE, CELL_SIZE)) # red normal food
    
    # draw of a snake
    for square in snake:
        pygame.draw.rect(screen, GREEN, (*square, CELL_SIZE, CELL_SIZE))

    # score render
    score_text = font.render(f"Score: {score}  Level: {level}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(speed)
    
    