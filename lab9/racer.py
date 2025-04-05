import pygame
import sys
import random
import time
from pygame.locals import *

# initializing
pygame.init()

# setting up FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# сreating colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

# constants for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEEDENEMY = 5
SPEEDCOIN = 6
SPEEDCOIN2 = 5
SCORE = 0
NUMBERCOIN = 0
COINS_TO_SPEED_UP = 5
ENEMY_SPEED_INCREMENT = 1

# fonts
font = pygame.font.Font(r'D:\codes\PP2\lab8\diploma.ttf', 90)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("obidno", True, BLACK)
background = pygame.image.load(r'D:\codes\PP2\lab8\AnimatedStreet.png')

# creating a white screen
DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game about tip kotori ot kopov bezhit")

# loading background music
pygame.mixer.music.load(r'D:\codes\PP2\lab8\GTA3OST] Aquasky (MSX FM) – Spectre (OST GTA 3).mp3')
pygame.mixer.music.play(-1)  # Start playing the music in a loop

# setting enemy
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"D:\codes\PP2\lab8\Car-Top-View-Transparent-Background.png")
        self.image = pygame.transform.scale(self.image, (77, 120))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0) 

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEEDENEMY)
        if (self.rect.bottom > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# setting Player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"D:\codes\PP2\lab8\mercedes-vid-s-verhu.png")
        self.image = pygame.transform.scale(self.image, (77, 120))
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520) 

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

# setting Coin
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"D:\codes\PP2\lab8\pngegg.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        self.state = False

    def move(self):
        global SPEEDCOIN
        self.rect.move_ip(0, SPEEDCOIN)
        if (self.rect.bottom > 600 or self.state):
            SPEEDCOIN = 6
            self.state = False
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Setting up Sprites
P1 = Player()
E1 = Enemy()
C1 = Coin()

# Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0, 0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))
    collect = font_small.render(str(NUMBERCOIN), True, BLACK)
    DISPLAYSURF.blit(collect, (SCREEN_WIDTH - 30, 10))

    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('D:\codes\PP2\lab8\crash.wav').play()
        time.sleep(1)

        DISPLAYSURF.fill(GRAY)
        DISPLAYSURF.blit(game_over, (60, 250))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(4)
        pygame.quit()
        sys.exit()

    if pygame.sprite.spritecollideany(P1, coins):
        NUMBERCOIN += 1
        SPEEDENEMY += ENEMY_SPEED_INCREMENT if NUMBERCOIN % COINS_TO_SPEED_UP == 0 else 0
        for entity in coins:
            entity.state = True

    pygame.display.update()
    FramePerSec.tick(FPS)