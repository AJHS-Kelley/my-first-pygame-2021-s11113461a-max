# Simple Animation with Pygame, Kelvin Jackson, 1/7/2022, 9:03, v0.6

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

# Set the box data
b1 = {'rect':pygame.Rect(300, 80, 50, 100), 'color':RED, 'dir':UPRIGHT}
b2 = {'rect':pygame.Rect(200, 200, 20, 20), 'color':GREEN, 'dir':UPLEFT}
b3 = {'rect':pygame.Rect(100, 150, 60, 60), 'color':BLUE, 'dir':DOWNLEFT}
boxes = [b1, b2, b3]

# Run the game loop.
while True:
    for event in pygame.event.get():
     if event.type == QUIT:
         pygame.quit()
         sys.exit()

    windowSurface.fill(WHITE)
    
    for b in boxes:
        # Move the box data structure
        if b['dir']== DOWNLEFT:
            b['rect'].left -= MOVESPEED
            b['rect'].top += MOVESPEED
        if b['dir']== DOWNRIGHT:
            b['rect'].left += MOVESPEED
            b['rect'].top += MOVESPEED
        if b['dir']== UPLEFT:
            b['rect'].left -= MOVESPEED
            b['rect'].top -= MOVESPEED
        if b['dir']== UPRIGHT:
            b['rect'].left += MOVESPEED
            b['rect'].top -= MOVESPEED

        if b['dir']== DOWNLEFT:
            # The box has moved past the top.
              if b['dir']== UPLEFT:
                  b['dir'] = DOWNLEFT
              if b['dir'] == DOWNRIGHT:
                  
          