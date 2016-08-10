import sys
import pygame
import pygame.locals
from random import randrange as random_randrange
from math import sin as math_sin, cos as math_cos, pi as math_pi
import func
import obj
import const
import game

def show_start_screen():

    play = False
    
    #Title
    titleFont = pygame.font.Font(const.BASICFONT, 100)
    
    titleSurf = titleFont.render('Asteroids', True, const.WHITE, const.BGCOLOR)
    displacement = 1
    state = 0

    #Buttons
    StartButton = obj.Button(const.DARKGREEN, const.GREEN, (const.WINDOW_WIDTH // 2 - 50, const.WINDOW_HEIGHT * 2 // 3, 100, 40))

    #Objects
    asteroid_list = []
    battleShip = obj.Ship([const.WINDOW_WIDTH // 2 - 55, 2 * const.WINDOW_HEIGHT // 3 - const.SPRITE_SHIP.get_height(), 10, 10])
    slow_ship = True
    
    pygame.key.set_repeat(1, 1)
    
    while not play:
        if random_randrange(25) == 0:
            asteroid_list.append( obj.Asteroid() )
        const.DISPLAYSURF.fill(const.BGCOLOR)
        titleRect = titleSurf.get_rect()
        titleRect.center = (const.WINDOW_WIDTH / 2, const.WINDOW_HEIGHT / 2 + displacement)
        
        for i in asteroid_list:
            i.move()

        battleShip.move(slow_ship)
        
        const.DISPLAYSURF.blit(titleSurf, titleRect)

        for i in asteroid_list:
            const.DISPLAYSURF.blit(i.image, i.location)

        const.DISPLAYSURF.blit( pygame.transform.rotate(battleShip.image, battleShip.angle), battleShip.blit_location )

        StartButton.Func('Start', const.WHITE, 20)

        #event loop
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                func.terminate()

            elif event.type==pygame.MOUSEBUTTONDOWN:
                if StartButton.Press():
                    play = True
                        
        pygame.display.update()
        const.FPSCLOCK.tick(15)
        if displacement > 10:
            state = 0
        elif displacement < -10:
            state = 1

        if state:
            displacement += 1
        else:
            displacement -= 1

    return play
