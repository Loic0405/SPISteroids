import pygame, sys
from pygame.locals import *
from random import randrange
from func import *
from object import *

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

def showStartScreen():

    global FPSCLOCK, DISPLAYSURF, BASICFONT

    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    BASICFONT = pygame.font.Font('resources\\freesansbold.ttf', 20)

    #Background Music
    music = pygame.mixer.music.load("resources\Defense Line.mp3")
    
    #Title
    titleFont = pygame.font.Font('resources\\freesansbold.ttf', 100)
    titleSurf = titleFont.render('Asteroids', True, WHITE, BGCOLOR)
    displacement = 1
    state = 0

    #Objects
    asteroid_list = []
    battleShip = Ship([WINDOW_WIDTH // 2 - 15, 2 * WINDOW_HEIGHT // 3, 10, 10])

    #Buttons
    StartButton = Button(DARKGREEN, GREEN, (WINDOW_WIDTH // 2 - 50, WINDOW_HEIGHT * 2 // 3, 100, 40))
   
    pygame.mixer.music.play()

    pygame.key.set_repeat(1, 1)
    
    while True:
        if randrange(25) == 0:
            asteroid_list.append( Asteroid() )
        DISPLAYSURF.fill(BGCOLOR)
        titleRect = titleSurf.get_rect()
        titleRect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 + displacement)
        
        for i in asteroid_list:
            i.Move()

        battleShip.Move()
        
        DISPLAYSURF.blit(titleSurf, titleRect)

        for i in asteroid_list:
            DISPLAYSURF.blit(i.image, i.location)

        DISPLAYSURF.blit(battleShip.image, battleShip.location)

        StartButton.Func('Start', WHITE, 20)

        #event loop
        
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

            elif event.type==pygame.MOUSEBUTTONDOWN:
                if StartButton.Press():
                    pass #start game

            elif event.type == pygame.KEYDOWN:
                if event.key == K_LEFT:
                    battleShip.acceleration[0] = -1

                elif event.key == K_RIGHT:
                    battleShip.acceleration[0] = 1

                elif event.key == K_DOWN:
                    battleShip.acceleration[1] = 1

                elif event.key == K_UP:
                    battleShip.acceleration[1] = -1

            
        
                        

        pygame.display.update()
        FPSCLOCK.tick(15)
        if displacement > 10:
            state = 0
        elif displacement < -10:
            state = 1

        if state:
            displacement += 1
        else:
            displacement -= 1
