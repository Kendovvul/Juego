class Personaje():

	def __init__(self, name, team, bag):

		self.__Name = name
		self.__Team = team
		self.__Bag = bag
		self.__Team_Full = True
		#self.__PC

	def getName(self):
		return self.__Name

	def getTeam(self):
		return self.__Team

	def getBag(self):
		return self.__Bag

	def Full(self):
		
		if len(self.__Team) == 6:
			self.__Team_Full = False
		
		return self.__Team_Full

	def addPokemon(self, Pokemon):
		if self.Full():
			self.__Team.append(Pokemon)
		else:
			pass