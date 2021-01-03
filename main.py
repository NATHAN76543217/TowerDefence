import pygame

if __name__ == "__main__":
	# The background color can be whatever you want
	(width, height) = (300, 200)
	background_colour = (0,255,255)
	screen = pygame.display.set_mode((width, height))
	# coucou
	pygame.display.set_caption('Tower defence')
	screen.fill(background_colour)
	pygame.display.flip()
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					running = False
				elif event.key == pygame.K_g:
					screen.fill((255, 255, 0))
					pygame.display.flip()

	pygame.quit()