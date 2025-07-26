import sys

import pygame
from pygame.locals import *

from Ball import Ball

# Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

# initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# load assets, images, etc.

# Initialize variables
oBall = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
# Loop forever
while True:
    # Check for and handle events
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Do any "per frame" actions
    oBall.update()

    # Clear the window
    window.fill(BLACK)

    # Draw all window elements
    oBall.draw()
    # Update the window
    pygame.display.update()

    # Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)
