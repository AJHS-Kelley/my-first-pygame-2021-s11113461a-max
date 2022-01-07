# Simple Animation with Pygame, Kelvin Jackson, 1/7/2022, 9:19, v0.2

from PyGamePractice import GREEN
import pygame, sys, time 
from pygame.locals import *

# Setup Pygame
pygame.inti()


WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Animation Example!')

# Setup the direction variable.
DOWNLEFT = 'down left'
DOWNRIGHT = 'downright'
UPLEFT = 'upleft'
UPRIGHT = 'upright'

MOVESPEED = 4


# Setup color values.
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)