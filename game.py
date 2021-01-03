class Game():
	def __init__(self):
		self.width = 0
		self.height = 0
		self.SizeH = 0
		self.SizeV = 0
		return
	
	def setWidth(self, width):
		self.width = width
	def setHeight(self, Height):
		self.height = Height

	def getWidth(self):
		return self.width
	def getHeight(self):
		return self.height
	   
	def setSizeH(self, SizeH):
		self.SizeH = SizeH
	def setSizeV(self, SizeV):
		self.SizeV = SizeV

	def getSizeH(self):
		return self.SizeH
	def getSizeV(self):
		return self.SizeV