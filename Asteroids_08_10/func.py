import sys
import pygame
import pygame.locals
import start_screen
import const

def textObjects(text, color, size):
    font = pygame.font.Font(const.BASICFONT, 20)
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
