import pygame
from ennemy import Ennemy

class Game():
	BLUE=(0, 0, 255)
	RED=(255, 0, 0)
	GREEN=(0, 255, 0)
	YELLOW=(255, 255, 0)
	BLACK=(0, 0, 0)
	WHITE=(255, 255, 255)
	def __init__(self):
		self.screen = None
		self.running = True
		self.width = 0
		self.height = 0
		self.nbCaseH = 0
		self.nbCaseV = 0
		self.caseW = 0
		self.caseH = 0
		self.map = None
		self.ennemies = []
		self.sponePoint = ()
		self.endPoint = ()
		self._waves = []
		return
	
	def __str__(self):
		string = "__GAME__" + \
			"\nS = " + str(self.sponePoint) + \
			"\nE = " + str(self.endPoint)
		return string
	#setter
	def setWidth(self, width):
		self.width = width
	def setHeight(self, Height):
		self.height = Height
	def setCaseW(self, width):
		self.caseW = width
	def setCaseH(self, height):
		self.caseH = height
	def setnbCaseH(self, nbCaseH):
		self.nbCaseH = nbCaseH
	def setnbCaseV(self, nbCaseV):
		self.nbCaseV = nbCaseV
	def setMap(self, my_map):
		if type(my_map) != list:
			return print("ERROR map type = " + str(type(my_map)))
		self.map = my_map
	def setScreen(self):
		self.screen = pygame.display.set_mode((self.width, self.height))
	def setWaves(self, waves):
		self._waves = waves
	def setSponePoint(self, tplxy):
		if type(tplxy) != tuple:
			raise TypeError("tplxy must be a Tuple")
		self.sponePoint = tplxy
	def setEndPoint(self, tplxy):
		if type(tplxy) != tuple:
			raise TypeError("tplxy must be a Tuple")
		self.endPoint = tplxy
	#getter
	def getSponePoint(self):
		return self.sponePoint
	def getEndPoint(self):
		return self.endPoint
	def getWidth(self):
		return self.width
	def getHeight(self):
		return self.height
	def getScreen(self):
		return self.screen
	def getnbCaseH(self):
		return self.nbCaseH
	def getnbCaseV(self):
		return self.nbCaseV
	#methods
	def handleEvents(self):
		"""
			update game propercies according to events
		"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					self.running = False
				elif event.key == pygame.K_g:
					self.screen.fill(self.YELLOW)
	def updateMap(self):
		"""
			update map display with new changes
		"""
		for y, line in enumerate(self.map):
			for x, case in enumerate(line):
				if (case == "0"):
					pygame.draw.rect(self.screen, self.BLUE, (x * self.caseW, y * self.caseH, self.caseW, self.caseH))
				elif (case == "1"):
					pygame.draw.rect(self.screen, self.RED, (x * self.caseW, y * self.caseH, self.caseW, self.caseH))
				else:
					pygame.draw.rect(self.screen, self.YELLOW, (x * self.caseW, y * self.caseH, self.caseW, self.caseH))
		for ennemy in self.ennemies:
			ennemy.move(self.map)
			ennemy.draw(self.screen)
		print(self.ennemies[0].direction)
		pygame.display.update()
	def generateEnnemies(self):
		En = []
		for dic in self._waves:
			for key in dic.keys():
				nbToCreate = dic[key]
				while nbToCreate > 0:
					En.append(Ennemy(100, self.sponePoint[0] * int(self.caseW) + int(self.caseW/2), self.sponePoint[1] * int(self.caseH) + int(self.caseH / 2), int(key), (self.caseW, self.caseH)))
					nbToCreate -= 1
		self.ennemies = En