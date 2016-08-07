import sys
import pygame
import pygame.locals
from random import randrange as random_randrange
import start_screen

def main():

    #pygame.init()
    pygame.display.set_caption('Asteroids')
    
    start_screen.show_start_screen()
    while True:
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()


main()
