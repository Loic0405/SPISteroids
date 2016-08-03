import pygame, sys
from pygame.locals import *
from random import randrange
from func import *

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

def play():
    DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    background = pygame.image.load('resources\\background.jpg').convert()

    #Background Music
    music = pygame.mixer.music.load("resources\Defense Line.mp3")

    #Objects
    asteroid_list = []
    battleShip = Ship((WINDOW_WIDTH // 2 - 33, WINDOW_HEIGHT // 2 - 44))


    
    
    
    
    
