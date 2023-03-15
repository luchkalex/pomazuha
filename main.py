import pygame
from utils import *
from settings import *
pygame.init()


current_screen = menu
run = True
while True:
    for event in pygame.event.get():
        action = current_screen.handle_event(event)
        if action == 'quit':
            pygame.quit()
            quit()
        elif action == 'play':
            print('Starting the game...')
        elif action == 'settings':
            current_screen = settings_screen
        
        
    current_screen.draw()
    pygame.display.update()