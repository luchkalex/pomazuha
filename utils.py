import pygame, os
pygame.init()
name = os.getlogin()

#COLORS
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 102, 204)
light_blue = (102, 255, 255)
light_green = (102, 255, 102)

#SETTINGS
WINDOW_SCALE = (1280, 720)
SCREEN = pygame.display.set_mode(WINDOW_SCALE)
pygame.display.set_caption(f"{name}, а ты хуй)")
icon = pygame.image.load("assets/png_icons/beer.png")
pygame.display.set_icon(icon)

BG = pygame.image.load("assets/menu_bg/menu1.jpg")
BG = pygame.transform.scale(BG, WINDOW_SCALE)

s = pygame.Surface((350, 720))
s.set_alpha(128)
s.fill(light_blue)


pygame.mixer.music.load("sounds/music/main_menu.mp3")
pygame.mixer.music.play()

#FONTS
title_font = pygame.font.Font("assets/fonts/nunito_bold.ttf", 60)
title_font.bold
menu_font = pygame.font.Font("assets/fonts/nunito_italic.ttf", 40)
menu_font.bold


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


menu = Menu()
menu.append_option('Start', lambda: print('huy'))
menu.append_option('Quit', quit)

def draw_menu():
    SCREEN.blit(BG, (0, 0))
    SCREEN.blit(s, (0, 0))
    draw_text("ROMA HUY", title_font, white, 50, 50)
    
    menu.draw(SCREEN, 50, 200, 75)