import pygame, sys
from pygame.locals import *
from random import randrange, uniform
from math import sqrt

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

BIGASTEROID1 = 0
BIGASTEROID2 = 1
BIGASTEROID3 = 2
BIGASTEROID4 = 3
BIGASTEROID5 = 4
ANASTEROID1 = 5
ANASTEROID2 = 6

class Asteroid(pygame.sprite.Sprite):


    
    def __init__(self):
        self.directionX = 0
        self.directionY = 0
        pygame.sprite.Sprite.__init__(self)
        
        #Type of asteroid
        self.type_asteroid = randrange(7)

        if self.type_asteroid == BIGASTEROID1:
            self.image = pygame.image.load('resources\\big_asteroid_1.png').convert_alpha()
        elif self.type_asteroid == BIGASTEROID2:
            self.image = pygame.image.load('resources\\big_asteroid_2.png').convert_alpha()
        elif self.type_asteroid == BIGASTEROID3:
            self.image = pygame.image.load('resources\\big_asteroid_3.png').convert_alpha()
        elif self.type_asteroid == BIGASTEROID4:
            self.image = pygame.image.load('resources\\big_asteroid_4.png').convert_alpha()
        elif self.type_asteroid == BIGASTEROID5:
            self.image = pygame.image.load('resources\\big_asteroid_5.png').convert_alpha()
        elif self.type_asteroid == ANASTEROID1:
            self.image = pygame.image.load('resources\\an_asteroid_1.png').convert_alpha()
        elif self.type_asteroid == ANASTEROID2:
            self.image = pygame.image.load('resources\\an_asteroid_2.png').convert_alpha()
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
        self.velocity = [0, 0]
        self.acceleration = [0, 0]

    def Move(self):
        self.location[0] += self.velocity[0]
        self.location[1] += self.velocity[1]

        if 0 > self.location[0] + self.image.get_width() // 2:
            self.location[0] = WINDOW_WIDTH - self.image.get_width() // 2
            
        elif self.location[0] + self.image.get_width() // 2 > WINDOW_WIDTH:
            self.location[0] = - self.image.get_width() // 2
            
        if 0 > self.location[1] + self.image.get_height() // 2:
            self.location[1] = WINDOW_HEIGHT - self.image.get_height() // 2
            
        elif self.location[1] + self.image.get_height() // 2 > WINDOW_HEIGHT:
            self.location[1] = - self.image.get_height() // 2

        self.velocity[0] += self.acceleration[0]
        self.velocity[1] += self.acceleration[1]

        if sqrt( self.velocity[0]**2 + self.velocity[1]**2 ) > 10:
            self.velocity[0] *= 10 / sqrt( self.velocity[0]**2 + self.velocity[1]**2 )
            self.velocity[1] *= 10 / sqrt( self.velocity[0]**2 + self.velocity[1]**2 )

        #if acceleration
        
        #reset acceleration
        self.acceleration[0] = 0
        self.acceleration[1] = 0

    def slow(self):
        if battleShip.velocity[0] != 0:
            battleShip.velocity[0] += -(battleShip.velocity[0] / abs(battleShip.velocity[0]) )
        if battleShip.velocity[1] != 0:
            battleShip.velocity[1] += -(battleShip.velocity[1] / abs(battleShip.velocity[1]) )
