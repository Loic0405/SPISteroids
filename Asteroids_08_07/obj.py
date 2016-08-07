"""This module constains the objects that are used in the game"""
import sys
import pygame
import pygame.locals
from random import randrange as random_randrange, uniform as random_uniform
from math import sin as math_sin, cos as math_cos, pi as math_pi, sqrt as math_sqrt
import const
import func

class Asteroid(pygame.sprite.Sprite):


    
    def __init__(self):
        self.directionX = 0
        self.directionY = 0
        pygame.sprite.Sprite.__init__(self)
        
        #Type of asteroid
        self.type_asteroid = random_randrange(7)

        if self.type_asteroid == const.BIG_ASTEROID1:
            self.image = const.SPRITE_B_AST1
        elif self.type_asteroid == const.BIG_ASTEROID2:
            self.image = const.SPRITE_B_AST2
        elif self.type_asteroid == const.BIG_ASTEROID3:
            self.image = const.SPRITE_B_AST3
        elif self.type_asteroid == const.BIG_ASTEROID4:
            self.image = const.SPRITE_B_AST4
        elif self.type_asteroid == const.BIG_ASTEROID5:
            self.image = const.SPRITE_B_AST5
        elif self.type_asteroid == const.AN_ASTEROID1:
            self.image = const.SPRITE_A_AST1
        elif self.type_asteroid == const.AN_ASTEROID2:
            self.image = const.SPRITE_A_AST2
            
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.location = [random_uniform(0, const.WINDOW_WIDTH - self.image.get_width()) ,0]

        if self.location[0] + self.image.get_width() > const.WINDOW_WIDTH:           
            self.directionX = random_uniform(-1, 1)
        else:
            self.directionX = random_uniform(-1, 2)

        if self.location[1] + self.image.get_height() > const.WINDOW_HEIGHT:
            self.directionY = random_uniform(-1, 1)
        elif self.location[1] + 1 < const.WINDOW_HEIGHT and self.directionX == 0:
            self.directionY = random_uniform(0, 2)
        else:
            self.directionY = random_uniform(0, 2)
        
    def move(self):
        self.location[0] += self.directionX
        self.location[1] += self.directionY


class Ship(pygame.sprite.Sprite):

    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = const.SPRITE_SHIP
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.location = location
        self.blit_location = location * 1
        self.angle = 0
        self.velocity = [0, 0]
        self.acceleration = [0, 0]

    def move(self):
        
        self.location[0] += self.velocity[0]
        self.location[1] += self.velocity[1]

        self.blit_location[0] = self.location[0] - abs(math_sin(math_pi*self.angle/90)*self.image.get_width()/math_sqrt(8))
        self.blit_location[1] = self.location[1] - abs(math_sin(math_pi*self.angle/90)*self.image.get_width()/math_sqrt(8))

        if 0 > self.location[0] + self.image.get_width() // 2:
            self.location[0] = const.WINDOW_WIDTH - self.image.get_width() // 2
            
        elif self.location[0] + self.image.get_width() // 2 > const.WINDOW_WIDTH:
            self.location[0] = - self.image.get_width() // 2
            
        if 0 > self.location[1] + self.image.get_height() // 2:
            self.location[1] = const.WINDOW_HEIGHT - self.image.get_height() // 2
            
        elif self.location[1] + self.image.get_height() // 2 > const.WINDOW_HEIGHT:
            self.location[1] = - self.image.get_height() // 2

        self.velocity[0] += self.acceleration[0]
        self.velocity[1] += self.acceleration[1]

        if math_sqrt( self.velocity[0]**2 + self.velocity[1]**2 ) > 10:
            self.velocity[0] *= 10 / math_sqrt( self.velocity[0]**2 + self.velocity[1]**2 )
            self.velocity[1] *= 10 / math_sqrt( self.velocity[0]**2 + self.velocity[1]**2 )

        
        #reset acceleration
        self.acceleration[0] = 0
        self.acceleration[1] = 0

    def slow(self):
        if battleShip.velocity[0] != 0:
            battleShip.velocity[0] += -(battleShip.velocity[0] / abs(battleShip.velocity[0]) )
        if battleShip.velocity[1] != 0:
            battleShip.velocity[1] += -(battleShip.velocity[1] / abs(battleShip.velocity[1]) )

class Button(object):
    def __init__(self, color, colorH, rect):
        self.color=color
        self.colorH=colorH
        self.rect = rect
        self.i=0
        
    def Draw(self):
        const.DISPLAYSURF.fill(self.color,rect=[self.rect[0],self.rect[1],self.rect[2],self.rect[3]])
        
    def Write(self,text,textcolor,textsize):
        textSurf,textRect= func.textObjects(text,textcolor,textsize)
        textRect.center=(self.rect[0]+self.rect[2]/2),(self.rect[1]+self.rect[3]/2)
        const.DISPLAYSURF.blit(textSurf,textRect)
        
    def Hover(self,text,textcolor,textsize):
        mousex,mousey=pygame.mouse.get_pos()
        if(self.rect[0]+self.rect[2]>=mousex>=self.rect[0] and self.rect[1]+self.rect[3]>=mousey>=self.rect[1]):
            const.DISPLAYSURF.fill(self.colorH,rect=[self.rect[0],self.rect[1],self.rect[2],self.rect[3]])
            self.Write(text,textcolor,textsize)
            
    def Press(self):
        val=False
        mousex,mousey=pygame.mouse.get_pos()
        if(self.rect[0]+self.rect[2]>=mousex>=self.rect[0] and self.rect[1]+self.rect[3]>=mousey>=self.rect[1]):
            val=True
        return val
    
    def Func(self,text,textcolor,textsize):
        self.Draw()
        self.Write(text,textcolor,textsize)
        self.Hover(text,textcolor,textsize)
