import sys
from pathlib import Path
from random import randrange

from pygame.locals import *

import pygame


# Define constants
BLACK = (0, 0, 0)
BASE_PATH = Path(__file__).resolve().parent
print('base path: ', BASE_PATH)
pathToBall = BASE_PATH / 'Images/ball.png'
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

# initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# load assets, images, etc.
ballImage = pygame.image.load(pathToBall)

# Initialize variables
ballPositionX = randrange(50, 600)
ballPositionY = randrange(50, 440)
ballRect = pygame.Rect(ballPositionX, ballPositionY, 100, 100)

# Loop forever
while True:
    # Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            # mouseX, mouseY = event.pos we could do that

            if ballRect.collidepoint(event.pos):
                ballPositionX = randrange(50, 600)
                ballPositionY = randrange(50, 440)
                ballRect = pygame.Rect(ballPositionX, ballPositionY, 100, 100)
        # Clicked the close button? Quit pygame and end program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Do any "per frame" actions

    # Clear the window
    window.fill(BLACK)

    # Draw all window elements
    window.blit(ballImage, (ballPositionX, ballPositionY))
    # Update the window
    pygame.display.update()

    # Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)
