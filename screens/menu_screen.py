import pygame
from utils import *
from screens.screen import *

class Menu(Screen):
    def __init__(self, screen_size, font, font_size, font_color, x, y, items):
        self.screen = pygame.display.set_mode(screen_size)
        self.font = pygame.font.SysFont(font, font_size)
        self.font_color = font_color
        self.x = x
        self.y = y
        self.items = items
        self.selected_item = 0

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            return 'quit'
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return 'quit'
            elif event.key == pygame.K_UP:
                self.selected_item = (self.selected_item - 1) % len(self.items)
            elif event.key == pygame.K_DOWN:
                self.selected_item = (self.selected_item + 1) % len(self.items)
            elif event.key == pygame.K_RETURN:
                if self.selected_item == 0:
                    return 'play'
                elif self.selected_item == 1:
                    return 'settings'
                elif self.selected_item == 2:
                    return 'quit'

    def draw(self):
        self.screen.blit(BG, (0, 0))

        for i in range(len(self.items)):
            item = self.items[i]
            text = self.font.render(item, True, self.font_color)
            text_rect = text.get_rect()
            text_rect.x = self.x
            text_rect.y = self.y + i * 50
            self.screen.blit(text, text_rect)

            if i == self.selected_item:
                pygame.draw.rect(self.screen, self.font_color, (text_rect.x - 10, text_rect.y - 5, text_rect.width + 20, text_rect.height + 10), 2)
