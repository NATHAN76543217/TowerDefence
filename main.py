import pygame
from game import Game
from ennemy import Ennemy

#à faire
#faire setter et getter de nbCaseH et nbCaseV
#cree rectangle de la bonne taille
#cree un rectangle pour toute les cases
def loadWave(gm, file):
	waves = []
	split = file.readline().split(" ")
	dic = {}
	for op in split[1:]:
		op = op.split(":")
		dic[op[0]] = int(op[1])
	waves.append(dic)
	return waves

def loadMap(gm, file):
	i = gm.getnbCaseV()
	my_map = []
	while (i > 0):
		line = file.readline()
		my_map.append([char for char in line[:-1]])
		i -= 1
	for y, line in enumerate(my_map):
		for x, char in enumerate(line):
			if char == "S":
				gm.setSponePoint((x,y))
			elif (char == "E"):
				gm.setEndPoint((x, y))
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
			gm.setnbCaseH(int(split_string[1]) - 1)
		elif split_string[0] == "SV":
			gm.setnbCaseV(int(split_string[1]))
		elif split_string[0] == "MAP":
			gm.setMap(loadMap(gm, file))
		elif split_string[0] == "WAVE":
			gm.setWaves(loadWave(gm, file))
		line = file.readline()
		split_string = line.split(" ")
	if (gm.getWidth() == 0 or gm.getHeight() == 0):
		print("ERROR height or width not found")
		return
	gm.setCaseW(gm.width /gm.nbCaseH)
	gm.setCaseH(gm.height/gm.nbCaseV)
	file.close()

if __name__ == "__main__":
	pygame.init()
	gm = Game()
	parseFile(gm)
	gm.setScreen() 
	pygame.display.set_caption('Tower defense')

	gm.screen.fill(gm.BLACK)
	pygame.display.flip()
	gm.generateEnnemies()
	print(gm)
	while gm.running:
		gm.handleEvents()
		gm.updateMap()
	pygame.quit()
