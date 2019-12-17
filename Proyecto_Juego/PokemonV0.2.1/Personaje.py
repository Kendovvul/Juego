class Personaje():

	def __init__(self, name, team, bag):

		self.__Name = name
		self.__Team = team
		self.__Bag = bag

	def getName(self):
		return self.__Name

	def getTeam(self):
		return self.__Team

	def getBag(self):
		return self.__Bag

	def addPokemon(self, Pokemon):
		self.__Team.append(Pokemon)