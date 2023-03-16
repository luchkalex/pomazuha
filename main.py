import pygame
from utils import *
from screens.settings_screen import *
pygame.init()

WINDOW_SCALE = (1280, 720)
menu = Menu(WINDOW_SCALE, 'Arial', 36, (255, 255, 255), 300, 200, ['Play', 'Settings', 'Quit'])

settings_screen = SettingsScreen(
    WINDOW_SCALE, 
    'Arial', 
    36, 
    (255, 255, 255), 
    300, 
    200, 
    ['Music', 'Sound Effects', 'Graphics Quality'], 
    [['On', 'Off'], ['On', 'Off'], 
    ['Low', 'Medium', 'High']], 
    [0, 0, 1])

current_screen: Screen = menu

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