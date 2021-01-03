import pygame
from game import Game
#à faire
#faire setter et getter de sizeH et sizeV
def readline(game):
	file = open('maps/map1.td', "r")
	line = file.readline()
	split_string = line.split(" ")
	while line:
		if split_string[0] == "R":
			game.setWidth(int(split_string[1]))
			game.setHeight(int(split_string[2]))
		#elif split_string[0] == "SH":
		#	game.setSizeH()
		line = file.readline()
		split_string = line.split(" ")

	print (game.getWidth(), game.getWidth())
	file.close()
	return game

if __name__ == "__main__":
	# The background color can be whatever you want
	gm = Game()
	readline(gm)
	background_colour = (255,0,0)
	print (gm.getWidth(), gm.getHeight())
	gm.setScreen() 
	pygame.display.set_caption('Tower defense')
	gm.screen.fill(background_colour)
	pygame.display.flip()

	BLUE=(0,0,255)
	pygame.draw.rect(gm.getScreen(), BLUE,(200,150,100,50))

	while gm.running:
		gm.handleEvents()
		pygame.display.update()
	pygame.quit()
