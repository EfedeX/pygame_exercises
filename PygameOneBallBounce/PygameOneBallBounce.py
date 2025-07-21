import sys
from pathlib import Path
from random import randrange

from pygame.locals import *

import pygame


# Define constants
BLACK = (0, 0, 0)
BASE_PATH = Path(__file__).resolve().parent
pathToBall = BASE_PATH / 'Images/ball.png'
pathToBounceSound = BASE_PATH / 'sounds/boing.wav'
pathToBgSound = BASE_PATH / 'sounds/background.mp3'
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
BALL_WIDTH_HEIGHT = 100
N_PIXELS_TO_MOVE = 3

# initialize the world
pygame.init()
pygame.mixer.init() 
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# load assets, images, etc.
ballImage = pygame.image.load(pathToBall)
bounceSound = pygame.mixer.Sound(pathToBounceSound)
pygame.mixer.music.load(pathToBgSound)
pygame.mixer.music.play(-1, 0.0)

# Initialize variables
ballRect = ballImage.get_rect()
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT
ballRect.left = randrange(MAX_WIDTH)
ballRect.right = randrange(MAX_HEIGHT)
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
    if (ballRect.left < 0) or (ballRect.right >= WINDOW_WIDTH):
        xSpeed = -xSpeed
        bounceSound.play()
    if (ballRect.top < 0) or (ballRect.bottom >= WINDOW_HEIGHT):
        ySpeed = -ySpeed
        bounceSound.play()

    ballRect.left = ballRect.left + xSpeed
    ballRect.top = ballRect.top + ySpeed

    # Clear the window
    window.fill(BLACK)

    # Draw all window elements
    window.blit(ballImage, ballRect)

    # Update the window
    pygame.display.update()

    # Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)
