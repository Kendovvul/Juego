class Item:

	def __init__ (self, name, Type, cost):
		self.__Name = name
		self.__Type = Type
		self.__Cost = cost

	def getName(self):
		return self.__Name

	def getType(self):
		return self.__Type

	def getCost(self):
		return self.__Cost

class Cures(Item):
	__Cure = 0

	def getCure(self):
		return self.__Cure

	def setCure(self, Cure):
		self.__Cure = Cure

class Potion(Cures):
	___Cantidad = 1

	def __init__(self):
		super(Potion, self).__init__("Potion", "Botiquin", 300)
		self.setCure(20)

	def Cantidad(self, cantidad):
		self.___Cantidad += cantidad