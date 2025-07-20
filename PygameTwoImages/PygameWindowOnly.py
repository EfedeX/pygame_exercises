import sys
from pathlib import Path
from random import randrange

from pygame.locals import *

import pygame


# Define constants
BLACK = (0, 0, 0)
BASE_PATH = Path(__file__).resolve().parent
pathToBall = BASE_PATH / 'Images/ball.png'
pathToTarget = BASE_PATH / 'Images/target.jpg'
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
TARGET_X = 400
TARGET_Y = 320
TARGET_WIDTH_HEIGHT = 120
N_PIXELS_TO_MOVE = 5

# initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# load assets, images, etc.
ballImage = pygame.image.load(pathToBall)
targetImage = pygame.image.load(pathToTarget)

# Initialize variables
ballPositionX = randrange(50, 600)
ballPositionY = randrange(50, 440)
targetRect = pygame.Rect(TARGET_X, TARGET_Y, TARGET_WIDTH_HEIGHT, TARGET_WIDTH_HEIGHT)
wasTouchingTarget = False

# Loop forever
while True:
    # Check for and handle events
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # elif event.type == pygame.KEYDOWN:
            # if event.key == pygame.K_LEFT:
            #     ballPositionX = ballPositionX - N_PIXELS_TO_MOVE
            # elif event.key == pygame.K_RIGHT:
            #     ballPositionX = ballPositionX + N_PIXELS_TO_MOVE
            # elif event.key == pygame.K_UP:
            #     ballPositionY = ballPositionY - N_PIXELS_TO_MOVE
            # elif event.key == pygame.K_DOWN:
            #     ballPositionY = ballPositionY + N_PIXELS_TO_MOVE
        
    # Do any "per frame" actions
    keyPressedTuple = pygame.key.get_pressed()
    if keyPressedTuple[pygame.K_a]:
        ballPositionX = ballPositionX - N_PIXELS_TO_MOVE
    if keyPressedTuple[pygame.K_d]:
        ballPositionX = ballPositionX + N_PIXELS_TO_MOVE
    if keyPressedTuple[pygame.K_w]:
        ballPositionY = ballPositionY - N_PIXELS_TO_MOVE
    if keyPressedTuple[pygame.K_s]:
        ballPositionY = ballPositionY + N_PIXELS_TO_MOVE

    ballRect = pygame.Rect(ballPositionX, ballPositionY, 100, 100)
    isTouching = ballRect.colliderect(targetRect)
    if wasTouchingTarget != isTouching:
        if isTouching:
            print("Ball is touching the target!")
        else:
            print("Ball is not touching the target!")
        wasTouchingTarget = isTouching

    # Clear the window
    window.fill(BLACK)

    # Draw all window elements
    window.blit(targetImage, (TARGET_X, TARGET_Y))
    window.blit(ballImage, (ballPositionX, ballPositionY))
    # Update the window
    pygame.display.update()

    # Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)
