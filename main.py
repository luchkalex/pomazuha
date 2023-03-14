import pygame, sys


WIDTH, HEIGHT = 1920, 1080
TEXT_COL = (255, 255, 255)

pygame.init()
font = pygame.font.SysFont("arialblack", 40)

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("pomazuha")

BG = pygame.image.load("assets/menu_bg/main_menu.jpg")
pygame.mixer.music.load("sounds/music/main_menu.mp3")
pygame.mixer.music.play()


def draw_text(text, font, text_col, x, y):
     img = font.render(text, True, text_col)
     SCREEN.blit(img, (x, y))

run = True
while run:
		SCREEN.fill([255, 255, 255])
		SCREEN.blit(BG, (0, 0))
		

		draw_text("Roma HUY", font, TEXT_COL, 50, 50)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		pygame.display.update()
pygame.quit()