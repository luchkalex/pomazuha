import pygame, sys


WIDTH, HEIGHT = 1280, 720
TEXT_COL = (255, 255, 255)

pygame.init()
font = pygame.font.SysFont("arialblack", 40)

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("pomazuha")

BG = pygame.image.load("assets\menu_bg\main_menu.jpg")

def draw_text(text, font, text_col, x, y):
     img = font.render(text, True, text_col)
     SCREEN.blit(img, (x, y))

run = True
while run:
		SCREEN.fill((52, 78, 92))

		draw_text("Roma HUY", font, TEXT_COL, 50, 50)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		pygame.display.update()
pygame.quit()