import pygame

class Ennemy():
	BLUE=(0, 0, 255)
	RED=(255, 0, 0)
	GREEN=(0, 255, 0)
	YELLOW=(255, 255, 0)
	QQC=(123, 200, 45)
	COLORS=[GREEN, YELLOW, QQC]
	SIZES=[10, 15, 17]
	SPEED=[0, 1, 2]
	def __init__(self, lifePoints, x, y, style, caseSize):
		self.life = lifePoints
		self.x = x
		self.y = y
		self.caseSize = caseSize
		self.px = int(self.x / caseSize[0])
		self.py = int(self.y / caseSize[1])
		self.direction = [0, 0]
		self.size = self.SIZES[style]
		self.color = self.COLORS[style]
		self.speed = self.SPEED[style]
		
	def draw(self, screen):
		pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)

	def move(self, mapp):
		if mapp[self.py-1][self.px] == "0" and self.direction[1] != 1:
			self.y -= 1 + self.speed
			self.direction[1] = -1
		elif mapp[self.py][self.px+1] == "0" and self.direction[0] != -1:
			self.x += 1 + self.speed
			self.direction[0] = 1
		elif mapp[self.py+1][self.px] == "0":
			self.y += 1 + self.speed
			self.direction[1] = 1
		elif mapp[self.py][self.px-1] == "0":
			self.x -= 1 + self.speed
			self.direction[0] = -1
		self.px = int((self.x - self.caseSize[0] / 2 * self.direction[0]) / self.caseSize[0])
		self.py = int((self.y - self.caseSize[1] / 2 * self.direction[1]) / self.caseSize[1])