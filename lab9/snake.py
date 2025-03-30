import pygame
import random

# Constants
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
WHITE, GREEN, BLACK, RED = (255, 255, 255), (0, 255, 0), (0, 0, 0), (255, 0, 0)

# Display initializing
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 15)
pygame.display.set_caption("Snake")

# Neccessary parameters
snake = [(100, 100), (90, 100), (80, 100)] # Head, body, tail
direction = (CELL_SIZE, 0)
food = (random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE))
score = 0
level = 1
speed = 15

# Food function (havchik, nyamka, SOTNI NYAMKI)
def spawn_food():
    while True:
        new_food = (random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE))
        if new_food not in snake:
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
    
    # draw of a snake
    pygame.draw.rect(screen, RED, (*food, CELL_SIZE, CELL_SIZE))
    for square in snake:
        pygame.draw.rect(screen, GREEN, (*square, CELL_SIZE, CELL_SIZE))

    # score render
    score_text = font.render(f"Score: {score}  Level: {level}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(speed)
    