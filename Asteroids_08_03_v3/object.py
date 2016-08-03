import pygame, sys
from pygame.locals import *
from random import randrange, uniform

WINDOW_WIDTH = 720
WINDOW_HEIGHT = 600

WHITE     = (255, 255, 255)
BLACK     = (  0,   0,   0)
RED       = (255,   0,   0)
GREEN     = (  0, 255,   0)
BLUE      = (  0,   0, 255)
YELLOW    = (255, 255,   0)
GRAY      = (100, 100, 100)
DARKGREEN = (  0, 155,   0)
DARKGRAY  = ( 40,  40,  40)
DARKBLUE  = (  0,   0, 155)
DARKYELLOW= (155, 155,   0)
BGCOLOR = BLACK


class Asteroid(pygame.sprite.Sprite):


    
    def __init__(self):
        self.directionX = 0
        self.directionY = 0
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources\\big_asteroid_1.png').convert_alpha()
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.location = [uniform(0, WINDOW_WIDTH - self.image.get_width()) ,0]

        if self.location[0] + self.image.get_width() > WINDOW_WIDTH:           
            self.directionX = uniform(-1, 1)
        else:
            self.directionX = uniform(-1, 2)

        if self.location[1] + self.image.get_height() > WINDOW_HEIGHT:
            self.directionY = uniform(-1, 1)
        elif self.location[1] + 1 < WINDOW_HEIGHT and self.directionX == 0:
            self.directionY = uniform(0, 2)
        else:
            self.directionY = uniform(0, 2)
        
    def Move(self):
        self.location[0] += self.directionX
        self.location[1] += self.directionY


class Ship(pygame.sprite.Sprite):

    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources\\battleship.png')
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.location = location

