import pygame

from screens.screen import *


class GameScreen(Screen):

    def __init__(self, screen_size, font, font_size, font_color, x, y):
        self.screen = pygame.display.set_mode(screen_size)
        self.font = pygame.font.SysFont(font, font_size)
        self.font_color = font_color
        self.x = x
        self.y = y

    def handle_event(self, event):
        pass

    def draw(self):
        pass
