class Attack:

    def __init__(self, name, Type, category, pp, power, accuracy):
        #self.MT_MO =

        self.__Name = name
        self.__Type = Type
        self.__Category = category
        self.__PP = pp
        self.__Power = power
        self.__Accuracy = accuracy
        #self.efecto
        #self.prioridad

        self.__Current_PP = pp
        self.__Current_Accuracy = accuracy

    #Getters de los valores fijos
    def getName(self):
        return self.__Name

    def getType(self, flag = 0):
        if flag == 0:
            return self.__Type[0]
        else:
            return self.__Type[1]

    def getCategory(self):
        return self.__Category

    def getPP(self):
        return self.__PP

    def getPower(self):
        return self.__Power

    def getAccuracy(self):
        return self.__Accuracy

    #Geters y Seters de los valores cambiantes
    def getCurrent_PP(self):
        return self.__Current_PP

    def Attack(self):
        self.__Current_PP -= 1

    def ResetCurrent_PP(self):
        self.__Current_PP = self.__PP

    def getCurrent_Accuracy(self):
        return self.__Current_Accuracy

    def ResetCurrent_Accuracy(self):
        self.__Current_Accuracy = self.__Accuracy