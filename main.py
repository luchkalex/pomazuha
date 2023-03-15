import pygame
from utils import *
pygame.init()


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
					elif event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
						menu.select()
		draw_menu()
		
		pygame.display.flip()
		
pygame.quit()