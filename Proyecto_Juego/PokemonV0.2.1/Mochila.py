from Objetos import *

class Mochila:

	def __init__(self):
		self.__OBJETOS = {}
		self.__BOTIQUIN = {}
		self.__MT_MO = {}
		self.__BAYAS = {}
		self.__OBJ_CLAVE = {}

	def addItem(self, item):

		if item.getType() == "Objeto":
			pass

		elif item.getType() == "Botiquin":
			if item.getName() not in self.__BOTIQUIN.keys():
				self.__BOTIQUIN[item.getName()] = item
			else:
				self.__BOTIQUIN[item.getName()].Cantidad()

		elif item.getType() == "MT" or item.getType() == "MO":
			pass

		elif item.getType() == "Baya":
			pass

		else:
			pass