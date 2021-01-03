import pygame
from game import Game
#à faire
#faire setter et getter de sizeH et sizeV
#cree rectangle de la bonne taille
#cree un rectangle pour toute les cases
def parseFile(gm):
	file = open('maps/map1.td', "r")
	line = file.readline()
	split_string = line.split(" ")
	while line:
		if split_string[0] == "R":
			gm.setWidth(int(split_string[1]))
			gm.setHeight(int(split_string[2]))
		elif split_string[0] == "SH":
			gm.setSizeH(int(split_string[1]))
		elif split_string[0] == "SV":
			gm.setSizeV(int(split_string[1]))
		line = file.readline()
		split_string = line.split(" ")

	file.close()

if __name__ == "__main__":
	# The background color can be whatever you want
	gm = Game()
	parseFile(gm)
	background_colour = (255,0,0)
	print (gm.getWidth(), gm.getHeight())
	screen = pygame.display.set_mode((gm.getWidth(), gm.getHeight()))
	# coucou
	pygame.display.set_caption('Tower defense')
	screen.fill(background_colour)
	pygame.display.flip()
	running = True
	BLUE=(0,0,255)
	coteH = (gm.width/gm.SizeH)
	coteV = (gm.height/gm.SizeV)
	pygame.draw.rect(screen, BLUE,(200,150,coteH,coteV))

	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					running = False
				elif event.key == pygame.K_g:
					screen.fill((255, 255, 0))
		pygame.display.update()

	pygame.quit()
