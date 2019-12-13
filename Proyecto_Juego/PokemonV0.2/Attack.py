class Attack:

    def __init__(self, name, tipo, category, pp, power, accuracy):
        #self.MT_MO =

        self.name = name
        self.tipo = tipo
        self.category = category
        self.pp = pp
        self.power = power
        self.accuracy = accuracy
        #self.efecto
        #self.prioridad

        self.Current_PP = pp
        self.Current_Power = power
        self.Current_Accuracy = accuracy