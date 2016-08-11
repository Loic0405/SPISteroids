import sys
import pygame
import pygame.locals
from random import randrange as random_randrange
import func
import start_screen
import game

def main():

    pygame.display.set_caption('Asteroids')
    var = start_screen.show_start_screen()
    
    if var:
        game.play()
        
    while True:
        for event in pygame.event.get(): # event handling loop
            if event.type == pygame.QUIT:
                func.terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    func.terminate()


main()
