### CONSTANTS
import pygame
import os

pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900, 500

WHITE = (255, 255 , 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

FPS = 60
VEL = 60
BULLET_VEL = 80
MAX_BULLETS = 10

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 70, 70

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game!")

BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)

BULLET_HIT_SOUND = pygame.mixer.Sound('space-classes/game/assets/Grenade+1.wav')
BULLET_FIRE_SOUND = pygame.mixer.Sound('space-classes/game/assets/Shot.wav')

HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)
