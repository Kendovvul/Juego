class Pokemon:

    def __init__ (self, name, type1, type2, stats, level, expb):
        self.name = name
        self.type1 = type1 #Tupla con un string con el nombre del tipo y con un numero de indice
        self.type2 = type2
        self.attacks = [] #ataques del pokemon
        self.stats = stats
        self.current_status = 0 ##quiza podrprint(damage)iamos cambiarlo
        self.Max_HP = self.Calculation_Max_HP(stats, level)
        self.current_HP = self.Max_HP
        self.level = level
        self.expbase = expb               #AGREGAR DSP EN CASO DE...
        self.xp = 0
        ##self.ID = id               AGREGAR DSP EN CASO DE...

    def Calculation_Max_HP(self, stats, level): 
        return int(10 + (((level/100) * (stats.HP * 2)) + stats.IVs + stats.EVs) + level) #PS: 10 + { Nivel / 100 x [ (Stat Base x 2) + IV + PE ] } + Nivel