import pygame
from utils import *
pygame.init()
     

menu = Menu()
menu.append_option('Start', lambda: print('huy'))
menu.append_option('Quit', quit)


run = True
while run:
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_w or event.key == pygame.K_UP:
						menu.switch(-1)
					elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
						menu.switch(1)
					elif event.key == pygame.K_SPACE:
						menu.select()

		

		SCREEN.blit(BG, (0, 0))
		draw_text("Roma HUY", menu_font, white, 50, 50)

		menu.draw(SCREEN, 100, 200, 75)

		
		pygame.display.update()
		
pygame.quit()