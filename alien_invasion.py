import sys
import pygame
from settings import Settings
from ship import Ship

def run_game():
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	ship = Ship(screen)
	bg_color = ai_settings.bg_color

	while True:
		for event in pygame.event.get():
			if event.type == pygame.quit:
				sys.exit()
			
			screen.fill(bg_color)
			ship.blitme()
			pygame.display.flip()

run_game()