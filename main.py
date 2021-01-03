import pygame
from game import Game
#à faire
#faire setter et getter de nbCaseH et nbCaseV
#cree rectangle de la bonne taille
#cree un rectangle pour toute les cases
def loadMap(gm, file):
	i = gm.getnbCaseV()
	my_map = []
	print("map = " + str(my_map))
	while (i > 0):
		line = file.readline()
		my_map.append([char for char in line])
		i -= 1
	print("map = " + str(my_map))
	return my_map

def parseFile(gm):
	file = open('maps/map1.td', "r")
	line = file.readline()
	split_string = line.split(" ")
	while line:
		if split_string[0] == "R":
			gm.setWidth(int(split_string[1]))
			gm.setHeight(int(split_string[2]))
		elif split_string[0] == "SH":
			gm.setnbCaseH(int(split_string[1]))
		elif split_string[0] == "SV":
			gm.setnbCaseV(int(split_string[1]))
		elif split_string[0] == "MAP":
			gm.setMap(loadMap(gm, file))
		line = file.readline()
		split_string = line.split(" ")
	if (gm.getWidth() == 0 or gm.getHeight() == 0):
		print("ERROR height or width not found")
		return
	gm.setCaseW(gm.width /gm.nbCaseH)
	gm.setCaseH(gm.height/gm.nbCaseV)
	file.close()

if __name__ == "__main__":
	# The background color can be whatever you want
	gm = Game()
	parseFile(gm)
	gm.setScreen() 
	pygame.display.set_caption('Tower defense')

	gm.screen.fill(gm.RED)
	pygame.display.flip()
	print("MAP")
	print(gm.map)
	while gm.running:
		gm.handleEvents()
		gm.updateMap()
	pygame.quit()
