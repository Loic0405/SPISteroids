import sys
import pygame
import pygame.locals
from random import randrange as random_randrange
from math import sin as math_sin, cos as math_cos, pi as math_pi
import func
import obj
import const

def play():
    
    #Objects
    asteroid_list = []
    bullet_list = []
    battleShip = obj.Ship((const.WINDOW_WIDTH // 2 - const.SPRITE_SHIP.get_width() //2 , const.WINDOW_HEIGHT // 2 - const.SPRITE_SHIP.get_height() // 2))
    slow_ship = True
    
    const.DISPLAYSURF.fill(const.BGCOLOR) #clear the screen

    #Music settings
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()
    pygame.key.set_repeat(1, 1)
    
    while True:
        if random_randrange(25) == 0:
            asteroid_list.append( obj.Asteroid() )
        const.DISPLAYSURF.fill(const.BGCOLOR)
              
        for i in asteroid_list:
            i.move()

        battleShip.move(slow_ship)

        for i in asteroid_list:
            const.DISPLAYSURF.blit(i.image, i.location)

        if len(bullet_list) != 0:
            for i in bullet_list:
                i.move(battleShip.image.get_width())
                const.DISPLAYSURF.blit(i.image, i.location)
                
        const.DISPLAYSURF.blit( pygame.transform.rotate(battleShip.image, battleShip.angle), battleShip.blit_location )

        #event loop
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                func.terminate()

            elif event.type == pygame.KEYDOWN:
                slow_ship = False
                
                if event.key == pygame.K_LEFT:
                    battleShip.angle += 3

                elif event.key == pygame.K_RIGHT:
                    battleShip.angle -= 3

                elif event.key == pygame.K_DOWN:
                    battleShip.acceleration = [math_sin(math_pi * battleShip.angle / 180), math_cos(math_pi * battleShip.angle / 180)]

                elif event.key == pygame.K_UP:
                    battleShip.acceleration = [-math_sin(math_pi * battleShip.angle / 180), -math_cos(math_pi * battleShip.angle / 180)]

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    bullet_list.append(obj.Bullet(battleShip.location[0] + const.SPRITE_SHIP.get_width() // 2 - const.SPRITE_BULLET.get_width() // 2,
                                                  battleShip.location[1] + const.SPRITE_SHIP.get_height() // 4, battleShip.angle))
                    const.BLAST.play()
                else:
                    slow_ship = True

        pygame.display.update()
        const.FPSCLOCK.tick(10)
