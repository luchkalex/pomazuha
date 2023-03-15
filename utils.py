import pygame, os
pygame.init()
# name = os.getlogin()

#COLORS
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 102, 204)
light_blue = (102, 255, 255)
light_green = (102, 255, 102)

#SETTINGS
WINDOW_SCALE = (1280, 720)
SCREEN = pygame.display.set_mode(WINDOW_SCALE)
OPTION_SCREEN = pygame.display.set_mode(WINDOW_SCALE)
current_screen = SCREEN
pygame.display.set_caption("pomazuha")
pygame.display.toggle_fullscreen()
icon = pygame.image.load("assets/png_icons/beer.png")
pygame.display.set_icon(icon)

BG = pygame.image.load("assets/menu_bg/menu1.jpg")
BG = pygame.transform.scale(BG, WINDOW_SCALE)

OPT_BG = pygame.image.load("assets/menu_bg/menu2.jpg")
OPT_BG = pygame.transform.scale(OPT_BG, WINDOW_SCALE)

s = pygame.Surface((390, 720))
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


def switch(boolbool):
    boolbool = not boolbool


# option = True
# option_menu = Menu()
# option_menu.append_option('Back', lambda: switch(option))


# def draw_options():
#     current_screen = OPTION_SCREEN
#     OPTION_SCREEN.blit(OPT_BG, (0, 0))
#     OPTION_SCREEN.blit(s, (0, 0))
#     draw_text("Roma Pidor", title_font, white, 50, 50)
#     option_menu.draw(OPTION_SCREEN, 50, 200, 75)


# def draw_menu(screen, menu_items):
#     for i, item in enumerate(menu_items):
#             color = white if i != current_item else (255, 0, 0)
#             text = menu_font.render(item, True, color)
#             x = 600 - text.get_width() // 2
#             y = 500 +i * 60
#             screen.blit(text, (x, y))


# main_menu_items = ['start', 'options', 'exit']
# current_item = 0

