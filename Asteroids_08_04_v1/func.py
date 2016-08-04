import pygame, sys
from pygame.locals import *
import start_screen

WINDOW_WIDTH = 720
WINDOW_HEIGHT = 600

DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

def textObjects(text, color, size):
    font = pygame.font.Font('resources\\Freesansbold.ttf', size)
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def checkForKeyPress():
    if len(pygame.event.get(QUIT)) > 0:
        terminate()

    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        terminate()
    #elif KeyUpEvents[0].key == K_SPACE:
        #start_game()
    return keyUpEvents[0].key        


def terminate():
    pygame.quit()
    sys.exit()

    
class Button(object):
    def __init__(self, color, colorH, rect):
        self.color=color
        self.colorH=colorH
        self.rect = rect
        self.i=0
        
    def Draw(self):
        DISPLAYSURF.fill(self.color,rect=[self.rect[0],self.rect[1],self.rect[2],self.rect[3]])
        
    def Write(self,text,textcolor,textsize):
        textSurf,textRect= textObjects(text,textcolor,textsize)
        textRect.center=(self.rect[0]+self.rect[2]/2),(self.rect[1]+self.rect[3]/2)
        DISPLAYSURF.blit(textSurf,textRect)
        
    def Hover(self,text,textcolor,textsize):
        mousex,mousey=pygame.mouse.get_pos()
        if(self.rect[0]+self.rect[2]>=mousex>=self.rect[0] and self.rect[1]+self.rect[3]>=mousey>=self.rect[1]):
            DISPLAYSURF.fill(self.colorH,rect=[self.rect[0],self.rect[1],self.rect[2],self.rect[3]])
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
