import pygame

class Game():
	def __init__(self):
		self.screen = None
		self.running = True
		self.width = 0
		self.height = 0
		return
	
	def setWidth(self, width):
		self.width = width
	def setHeight(self, Height):
		self.height = Height

	def getWidth(self):
		return self.width
	def getHeight(self):
		return self.height
	def setScreen(self):
		self.screen = pygame.display.set_mode((self.getWidth(), self.getHeight()))
	def getScreen(self):
		return self.screen
	def handleEvents(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					self.running = False
				elif event.key == pygame.K_g:
					self.screen.fill((255, 255, 0))
		