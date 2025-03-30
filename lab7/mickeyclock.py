import pygame
import datetime
pygame.init()

screen = pygame.display.set_mode((829, 836))
clock = pygame.time.Clock()
pygame.display.set_caption("Mickey Clock")

mickey = pygame.image.load(r'D:\codes\PP2\lab7\mickey_clock_img\main-clock.png')
minutes = pygame.image.load(r'D:\codes\PP2\lab7\mickey_clock_img\right-hand.png')
seconds = pygame.image.load(r'D:\codes\PP2\lab7\mickey_clock_img\left-hand.png')

surface_center = mickey.get_rect().center
minn = minutes.get_rect(center = surface_center)
secc = seconds.get_rect(center = surface_center)
angle1 = 0
angle2 = 0

screen.blit(mickey, (0, 0))
pygame.display.update()

done = False
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
    now = datetime.datetime.now().time()
    minute = now.minute
    second = now.second

    angle1 = -minute * 6 + 84
    rot1 = pygame.transform.rotate(minutes, angle1)
    rect1 = rot1.get_rect()
    rect1.center = minn.center
    
    angle2 = -second * 6 - 275
    rot2 = pygame.transform.rotate(seconds, angle2)
    rect2 = rot2.get_rect()
    rect2.center = secc.center

    screen.blit(mickey, (0, 0))
    screen.blit(rot1, rect1)
    screen.blit(rot2, rect2)

    pygame.display.flip()
    clock.tick(60)

