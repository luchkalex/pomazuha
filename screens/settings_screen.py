import pygame
from utils import *
from screens.screen import *

class SettingsScreen(Screen):
    def __init__(self, screen_size, font, font_size, font_color, x, y, settings, options, selected_option):
        self.screen = pygame.display.set_mode(screen_size)
        self.font = pygame.font.SysFont(font, font_size)
        self.font_color = font_color
        self.x = x
        self.y = y
        self.settings = settings
        self.options = options
        self.selected_option = selected_option
        self.selected_menu = 0

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            return 'quit'
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return 'quit'
            elif event.key == pygame.K_UP:
                self.selected_menu = (self.selected_menu - 1) % len(self.settings)
            elif event.key == pygame.K_DOWN:
                self.selected_menu = (self.selected_menu + 1) % len(self.settings)
            elif event.key == pygame.K_RETURN:
                if self.selected_menu == 0:
                    # обрабатываем выбранную опцию для музыки
                    if self.selected_option[self.selected_menu] == 0:
                        self.selected_option[self.selected_menu] = 1
                        print('Music turned on')
                    elif self.selected_option[self.selected_menu] == 1:
                        self.selected_option[self.selected_menu] = 0
                        print('Music turned off')
                elif self.selected_menu == 1:
                    # обрабатываем выбранную опцию для звуковых эффектов
                    if self.selected_option[self.selected_menu] == 0:
                        self.selected_option[self.selected_menu] = 1
                        print('Sound effects turned on')
                    elif self.selected_option[self.selected_menu] == 1:
                        self.selected_option[self.selected_menu] = 0
                        print('Sound effects turned off')
                elif self.selected_menu == 2:
                    # обрабатываем выбранную опцию для качества графики
                    if self.selected_option[self.selected_menu] == 0:
                        self.selected_option[self.selected_menu] = 1
                        print('Graphics quality set to low')
                    elif self.selected_option[self.selected_menu] == 1:
                        self.selected_option[self.selected_menu] = 2
                        print('Graphics quality set to medium')
                    elif self.selected_option[self.selected_menu] == 2:
                        self.selected_option[self.selected_menu] = 0
                        print('Graphics quality set to high')

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mx, my = event.pos
                for i in range(len(self.settings)):
                    text_rect = self.font.render(self.settings[i], True, self.font_color).get_rect()
                    text_rect.x = self.x
                    text_rect.y = self.y + i * 50
                    if text_rect.collidepoint(mx, my):
                        self.selected_menu = i

    def draw(self):
        self.screen.blit(BG, (0, 0))

        for i in range(len(self.settings)):
            text = self.font.render(self.settings[i], True, self.font_color)
            text_rect = text.get_rect()
            text_rect.x = self.x
            text_rect.y = self.y + i * 50
            self.screen.blit(text, text_rect)

            for j in range(len(self.options[i])):
                option = self.options[i][j]
                option_text = self.font.render(option, True, self.font_color)
                option_rect = option_text.get_rect()
                option_rect.x = self.x + text_rect.width + 20 + j * 100
                option_rect.y = self.y + i * 50
            if i == self.selected_menu:
                pygame.draw.rect(self.screen, self.font_color, (text_rect.x - 10, text_rect.y - 5, text_rect.width + 20, text_rect.height + 10), 2)