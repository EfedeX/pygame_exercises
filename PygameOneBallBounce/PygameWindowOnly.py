import sys
from pathlib import Path
from random import randrange

from pygame.locals import *

import pygame


# Define constants
BLACK = (0, 0, 0)
BASE_PATH = Path(__file__).resolve().parent
pathToBall = BASE_PATH / 'Images/ball.png'
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
BALL_WIDTH_HEIGHT = 100
N_PIXELS_TO_MOVE = 3

# initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# load assets, images, etc.
ballImage = pygame.image.load(pathToBall)

# Initialize variables
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT
ballX = randrange(50, 600)
ballY = randrange(50, 440)
xSpeed = N_PIXELS_TO_MOVE
ySpeed = N_PIXELS_TO_MOVE

# Loop forever
while True:
    # Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    # Do any "per frame" actions
    if (ballX < 0) or (ballX >= MAX_WIDTH):
        xSpeed = -xSpeed
    if (ballY < 0) or (ballY >= MAX_HEIGHT):
        ySpeed = -ySpeed

    ballX += xSpeed
    ballY += ySpeed

    # Clear the window
    window.fill(BLACK)

    # Draw all window elements
    window.blit(ballImage, (ballX, ballY))

    # Update the window
    pygame.display.update()

    # Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)
