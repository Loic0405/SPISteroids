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

    list_explosion = []

    lives = 2
    lives_string = 'Lives: ' + str(lives)
    lives_font = pygame.font.Font(const.BASICFONT, 20)
    lives_surf = lives_font.render(lives_string, True, const.WHITE)
    lives_rect = lives_surf.get_rect()
    lives_rect.center = (lives_surf.get_width(), const.WINDOW_HEIGHT - lives_surf.get_height())
                                  
    score = 0
    score_string = 'Score: ' + str(score)
    score_font = pygame.font.Font(const.BASICFONT, 20)
    score_surf = score_font.render(score_string, True, const.WHITE)
    score_rect = score_surf.get_rect()
    score_rect.center = (const.WINDOW_WIDTH - score_surf.get_width(), const.WINDOW_HEIGHT - score_surf.get_height())
    
    const.DISPLAYSURF.fill(const.BGCOLOR) #clear the screen

    #Music settings
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play()
    
    while lives > 0:
        
        #Generating the asteroids
        if random_randrange(15) == 0:
            asteroid_list.append( obj.Asteroid() )
            
        const.DISPLAYSURF.fill(const.BGCOLOR)
        const.DISPLAYSURF.blit(const.BG, (0,0))
              
        for i in asteroid_list:
            i.move()
            
        if len(bullet_list) != 0:
            for i in bullet_list:
                if battleShip != 0:
                    i.move(battleShip.image.get_width())
                    const.DISPLAYSURF.blit(i.image, i.location)
                
                for j in asteroid_list:
                    if i.check_collision(j):
                        asteroid_list.remove(j)
                        bullet_list.remove(i)
                        list_explosion.append(obj.Explosion(j))
                        score += 1
                        break
                    
        if battleShip != 0:
            battleShip.move(slow_ship)
            const.DISPLAYSURF.blit( pygame.transform.rotate(battleShip.image, battleShip.angle), battleShip.blit_location )
            for i in asteroid_list:
                if battleShip != 0:
                    if battleShip.check_collision(i):
                        pos_exp = battleShip.location
                        battleShip = 0
                        lives -= 1
                        for j in range(len(asteroid_list)):
                            asteroid_list.pop()

                        for i in const.EXP_LIST:
                            const.DISPLAYSURF.fill(const.BGCOLOR)
                            const.DISPLAYSURF.blit(const.BG, (0,0))
                            const.DISPLAYSURF.blit(i, pos_exp)
                            pygame.display.update()
                            const.FPSCLOCK.tick(15)
                            
                            
                else:
                    continue

        for i in asteroid_list:
            const.DISPLAYSURF.blit(i.image, i.location)

        score_string = 'Score: ' + str(score)
        score_surf = score_font.render(score_string, True, const.WHITE)
        const.DISPLAYSURF.blit(score_surf, score_rect)

        lives_string = 'Lives: ' + str(lives)
        lives_surf = lives_font.render(lives_string, True, const.WHITE)
        const.DISPLAYSURF.blit(lives_surf, lives_rect)

        if len(list_explosion) != 0:
            for i in list_explosion:
                i.draw()

        #event loop
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                func.terminate()

            if battleShip == 0:
                battleShip = obj.Ship((const.WINDOW_WIDTH // 2 - const.SPRITE_SHIP.get_width() //2 , const.WINDOW_HEIGHT // 2 - const.SPRITE_SHIP.get_height() // 2))

            else:

                list_key = []
                list_key = pygame.key.get_pressed()
                
                if len(list_key) != 0:
                
                    slow_ship = True
                    
                    if list_key[pygame.K_LEFT]:
                        battleShip.angle += 10
                        slow_ship = False

                    if list_key[pygame.K_RIGHT]:
                        battleShip.angle -= 10
                        slow_ship = False

                    if list_key[pygame.K_DOWN]:
                        battleShip.acceleration = [math_sin(math_pi * battleShip.angle / 180), math_cos(math_pi * battleShip.angle / 180)]
                        slow_ship = False
                    
                    if list_key[pygame.K_UP]:
                        battleShip.acceleration = [-math_sin(math_pi * battleShip.angle / 180), -math_cos(math_pi * battleShip.angle / 180)]
                        slow_ship = False

                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_SPACE:
                            bullet_list.append(obj.Bullet(battleShip.location[0] + const.SPRITE_SHIP.get_width() // 2 - const.SPRITE_BULLET.get_width() // 2,
                                                          battleShip.location[1] + const.SPRITE_SHIP.get_height() // 4, battleShip.angle))
                            const.BLAST.play()

        #delete the bullets that can't be seen on the screen
        for i in bullet_list:
            if i.location[0] < 0 or i.location[0] > const.WINDOW_WIDTH\
               or i.location[1] < 0 or i.location[1] > const.WINDOW_HEIGHT:
                bullet_list.remove(i)

        #Same for asteroids
        for i in asteroid_list:
            if i.location[0] + i.image.get_width() < 0 or i.location[0] - i.image.get_width() > const.WINDOW_WIDTH\
               or i.location[1] + i.image.get_height() < 0 or i.location[1] - i.image.get_height() > const.WINDOW_HEIGHT:
                asteroid_list.remove(i)

        for i in list_explosion:
            if i.size > 30:
                list_explosion.remove(i)
                
        pygame.display.update()
        const.FPSCLOCK.tick(15)
        
    pygame.mixer.music.stop()
    game_over()

def game_over(): #Will take the score as a parameter to show it at the end of the game
    #Text
    game_over_font = pygame.font.Font(const.BASICFONT, 100)
    replay_font = pygame.font.Font(const.BASICFONT, 70)
    game_over_surf = game_over_font.render('Game Over', True, const.WHITE)
    replay_surf = replay_font.render('Press Enter to play again', True, const.WHITE)
    game_over_rect = game_over_surf.get_rect()
    replay_rect = replay_surf.get_rect()
    game_over_rect.center = (const.WINDOW_WIDTH / 2, const.WINDOW_HEIGHT / 2)
    replay_rect.center = (const.WINDOW_WIDTH / 2, const.WINDOW_HEIGHT / 2 + game_over_surf.get_height())

    const.DISPLAYSURF.fill(const.BGCOLOR)
    const.DISPLAYSURF.blit(const.BG, (0,0))
    const.DISPLAYSURF.blit(game_over_surf, game_over_rect)
    const.DISPLAYSURF.blit(replay_surf, replay_rect)

    while True:
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                func.terminate()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    play()
                elif event.key == pygame.K_ESCAPE:
                    func.terminate()
                    
         pygame.display.update()
