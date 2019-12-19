from Objetos import *

class Mochila:

	def __init__(self):
		self.__OBJETOS = {}
		self.__BOTIQUIN = {}
		self.__MT_MO = {}
		self.__BAYAS = {}
		self.__OBJ_CLAVE = {}

#####################################################################################

	def addItem(self, item):

		if item.getType() == "Objeto":
			if item.getName() not in self.__BOTIQUIN.keys():
				self.__OBJETOS[item.getName()] = item
			else:
				self.__OBJETOS[item.getName()].Cantidad()

		elif item.getType() == "Botiquin":
			if item.getName() not in self.__BOTIQUIN.keys():
				self.__BOTIQUIN[item.getName()] = item
			else:
				self.__BOTIQUIN[item.getName()].Cantidad()

		elif item.getType() == "MT" or item.getType() == "MO":
			if item.getName() not in self.__BOTIQUIN.keys():
				self.__MT_MO[item.getName()] = item
			else:
				self.__MT_MO[item.getName()].Cantidad()

		elif item.getType() == "Baya":
			if item.getName() not in self.__BOTIQUIN.keys():
				self.__BAYAS[item.getName()] = item
			else:
				self.__BAYAS[item.getName()].Cantidad()

		else:
			if item.getName() not in self.__BOTIQUIN.keys():
				self.__OBJ_CLAVE[item.getName()] = item
			else:
				self.__OBJ_CLAVE[item.getName()].Cantidad()

#######################################################################################

	def Objetos(self):
		pass

#######################################################################################

	def Botiquin(self, Pokemons):
		cont = 1
		flag = True
		while flag:

			Objetos = []

			for item in self.__BOTIQUIN.keys():
				print("("+str(cont)+")",item+"........"+str(self.__BOTIQUIN[item].getCantidad()))
				Objetos.append(item)

			comando = input()

			print("(1) Usar (2) Atras")

			Usar = input()

			if Usar == "1":
				print("¿Elige a quien curar?")
				index_pokemon = 1
				for pkm in Pokemons:
					print("("+str(index_pokemon)+")", pkm.getName())
					index_pokemon += 1
				
				index_pokemon = int(input())
				
				Pokemons[index_pokemon-1].Cure(cure = self.__BOTIQUIN[Objetos[int(comando)-1]].getCure())
				print(Pokemons[index_pokemon-1].getName(), 
					str(Pokemons[index_pokemon-1].getCurrent_HP())+"/"+str(Pokemons[index_pokemon-1].getMax_HP()))
				return 
					
			else: 
				pass

##############################################################################################

	def MT_MO(self):
		pass

	def Bayas(self):
		pass

	def OBJ_Clave(self):
		pass