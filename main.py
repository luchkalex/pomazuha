import pygame, sys, os
pygame.init()


WINDOW_SCALE = (1280, 720)
TEXT_COL = (255, 255, 255)

font = pygame.font.SysFont("arialblack", 40)

SCREEN = pygame.display.set_mode(WINDOW_SCALE)
pygame.display.set_caption("pomazuha")

BG = pygame.image.load("assets/menu_bg/menu1.jpg")
BG = pygame.transform.scale(BG, WINDOW_SCALE)

pygame.mixer.music.load("sounds/music/main_menu.mp3")
pygame.mixer.music.play()


def draw_text(text, font, text_col, x, y):
     img = font.render(text, True, text_col)
     SCREEN.blit(img, (x, y))


run = True
while run:
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False
		

		SCREEN.blit(BG, (0, 0))
		draw_text("Roma HUY", font, TEXT_COL, 50, 50)

		
		

		pygame.display.update()
	


		
		
pygame.quit()