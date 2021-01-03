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
	gm.setScreen() 
	pygame.display.set_caption('Tower defense')
	gm.screen.fill(background_colour)
	pygame.display.flip()

	BLUE=(0,0,255)
	coteH = (gm.width/gm.SizeH)
	coteV = (gm.height/gm.SizeV)
	pygame.draw.rect(gm.getScreen(), BLUE,(200,150,coteH,coteV))

	while gm.running:
		gm.handleEvents()
		pygame.display.update()
	pygame.quit()
