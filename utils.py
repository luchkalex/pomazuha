import pygame
pygame.init()

#COLORS
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 102, 204)

#SETTINGS
WINDOW_SCALE = (1280, 720)
SCREEN = pygame.display.set_mode(WINDOW_SCALE)
pygame.display.set_caption("pomazuha")

BG = pygame.image.load("assets/menu_bg/menu1.jpg")
BG = pygame.transform.scale(BG, WINDOW_SCALE)

pygame.mixer.music.load("sounds/music/main_menu.mp3")
pygame.mixer.music.play()

menu_font = pygame.font.SysFont("arialblack", 40)


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    SCREEN.blit(img, (x, y))
    

class Menu:
    def __init__(self):
        self._option_surfaces = []
        self._callbacks = []
        self._curent_option_index = 0

    
    def append_option(self, option, callback):
        self._option_surfaces.append(menu_font.render(option, True, white))
        self._callbacks.append(callback)

    
    def switch(self, direction):
        self._curent_option_index = max(0, min(self._curent_option_index + direction, len(self._option_surfaces) - 1))



    def select(self):
        self._callbacks[self._curent_option_index]()


    def draw(self, surf, x, y, option_y_padding):
        for i, option in enumerate(self._option_surfaces):
            option_rect = option.get_rect()
            option_rect.topleft = (x, y + i * option_y_padding)
            if i == self._curent_option_index:
                pygame.draw.rect(surf, (0, 100, 0), option_rect)
            surf.blit(option, option_rect)