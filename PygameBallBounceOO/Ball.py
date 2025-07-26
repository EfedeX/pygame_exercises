from pathlib import Path
import random

import pygame
from pygame.locals import *


class Ball:
    def __init__(self, window, windowWidth: int, windowHeight: int):
        self.window = window
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight

        self.image = pygame.image.load(Path(__file__).resolve().parent / 'images' / 'ball.png')
        ballRect = self.image.get_rect()
        self.width = ballRect.width
        self.height = ballRect.height
        self.maxWidth = self.windowWidth - ballRect.width
        self.maxHeight = self.windowHeight - ballRect.height

        self.x = random.randrange(20, self.maxWidth)
        self.y = random.randrange(20, self.maxHeight)
        speedsList = range(-4, 5)
        self.xSpeed = random.choice(speedsList)
        self.ySpeed = random.choice(speedsList)

    def update(self):
        if (self.x < 1) or (self.x >= self.maxWidth):
            self.xSpeed = -self.xSpeed
        if (self.y < 1) or (self.y >= self.maxHeight):
            self.ySpeed = -self.ySpeed
        self.x += self.xSpeed
        self.y += self.ySpeed

    def draw(self):
        self.window.blit(self.image, (self.x, self.y))