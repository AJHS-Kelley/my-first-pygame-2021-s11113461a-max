# PyGame Collision Derection Practice, Kelvin Jackson, January 04,2022, 10:05am, v0.2

import pygame, sys, random
from pygame.locals import *

 # Setup Pygame
 pygame.init()
 mainClock = pygame.time.Clock()

 # Setup the PyGame Window
 WINDOWWIDTH = 400
 WINDOWHEIGHT = 400 
 windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
 pygame.display.set_caption('Collision Detection 2022')

 # Setup colors.
 BLACK = (0, 0, 0)
 GREEN = (0, 255, 0)
 WHITE = (255, 255, 255)
 