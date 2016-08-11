"""This file contains all the constants
that are used in the code"""

import os
import pygame
import pygame.locals
import pygame.mixer

pygame.mixer.init(48000, -16, 2, 2048)
pygame.init()

#Size of the window
WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 700

#Colors
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

#pygame constants
FPSCLOCK = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
BASICFONT = 'resources\\FreeSansBold.ttf'

#Music and sounds
BGMUSIC = pygame.mixer.music.load("resources\\music.ogg")
BLAST = pygame.mixer.Sound("resources\\small_blast.ogg")

#Type of Asteroids
BIG_ASTEROID1 = 0
BIG_ASTEROID2 = 1
BIG_ASTEROID3 = 2
BIG_ASTEROID4 = 3
BIG_ASTEROID5 = 4
AN_ASTEROID1 = 5
AN_ASTEROID2 = 6

#Sprites
SPRITE_SHIP = pygame.image.load('resources\\battleship.png')
SPRITE_B_AST1 = pygame.image.load('resources\\big_asteroid_1.png').convert_alpha()
SPRITE_B_AST2 = pygame.image.load('resources\\big_asteroid_2.png').convert_alpha()
SPRITE_B_AST3 = pygame.image.load('resources\\big_asteroid_3.png').convert_alpha()
SPRITE_B_AST4 = pygame.image.load('resources\\big_asteroid_4.png').convert_alpha()
SPRITE_B_AST5 = pygame.image.load('resources\\big_asteroid_5.png').convert_alpha()
SPRITE_A_AST1 = pygame.image.load('resources\\an_asteroid_1.png').convert_alpha()
SPRITE_A_AST2 = pygame.image.load('resources\\an_asteroid_2.png').convert_alpha()
SPRITE_BULLET = pygame.image.load('resources\\bullet.png').convert_alpha()

#Background image
BG = pygame.image.load('resources\\background.jpg').convert()

