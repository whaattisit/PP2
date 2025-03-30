import pygame

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Circle")
done = False
x = 800//2
y = 400//2
radius = 25
v = 20
clock = pygame.time.Clock()
while not done:
    clock.tick(100)
    screen.fill((255, 255, 255))
    circle = pygame.draw.circle(screen,(200, 0, 0), (x, y), radius)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and x > radius:
                x -= v
            if event.key == pygame.K_RIGHT and x < 800 - radius:
                x += v
            if event.key == pygame.K_UP and y > radius:
                y -= v
            if event.key == pygame.K_DOWN and y < 400 - radius:
                y += v
            