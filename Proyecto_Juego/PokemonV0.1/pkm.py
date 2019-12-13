import random

class Pokemon:

    def __init__ (self, name, type1, type2, stats, level, expb):
        self.name = name
        self.type1 = type1
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

    
class Stats:

    def __init__(self, HP, Attack, Defense, SpAttack, SpDefense, Speed):

        self.IVs = 3
        self.EVs = 1
        self.HP = HP
        self.Attack = Attack
        self.Defense = Defense
        self.SpAttack = SpAttack
        self.SpDefense = SpDefense
        self.Speed = Speed

class Attack:

    def __init__(self, name, tipo, category, pp, power, accuracy):
        self.name = name
        self.tipo = tipo
        self.category = category
        self.pp = pp
        self.power = power
        self.accuracy = accuracy
        #self.efecto
        #self.prioridad

class Battle:

    def __init__(self, pkm1, pkm2, typec):
        self.pokemon1 = pkm1
        self.pokemon2 = pkm2
        self.actual_turn = 0
        self.typec = typec  ##char s : salvaje , e: entrenador
        self.winner = None
        self.loser = None

    def Calculation_Damage(self, pkm1, pkm2, index_attack):
        Bonus = 1
        Effectiveness = 1
        Varation = random.uniform(85, 100)
        Level = pkm1.level
        Power = pkm1.attacks[index_attack].power

        if(pkm1.attacks[index_attack].category == "fisico"):
            Attack = pkm1.stats.Attack
            Defense = pkm2.stats.Defense
        else:
            Attack = pkm1.stats.SpAttack
            Defense = pkm2.stats.SpDefense

        if (pkm1.attacks[index_attack].tipo == pkm2.type1 or pkm1.attacks[index_attack].tipo == pkm2.type2):
            Bonus = 1.5


        damage = 0.01 * Bonus * Varation * (((((0.2 * Level)+2) * Attack * Power)/(25 * Defense))+2)
        print("Damage:", int(damage))
        return int(damage)

    def action(self, pkm1, pkm2, index_attack):

        print(pkm1.name, "ha usado", pkm1.attacks[index_attack].name)
        pkm2.current_HP -= self.Calculation_Damage(pkm1, pkm2, index_attack)
        
        if pkm2.current_HP<=0:
            pkm2.current_HP = 0
            print(pkm2.name,":",pkm2.current_HP)
            return
        print(pkm2.name,":",pkm2.current_HP)

    def combat(self, pkm1, pkm2):

        print("Que debe hacer", pkm1.name+"?")
        comando = input().split(" ")
        index_attack = int(comando[1])

        if comando[0] == "ataque" and index_attack < 4 and index_attack <= len(pkm1.attacks):
            if pkm1.stats.Speed > pkm2.stats.Speed:
                self.action(pkm1, pkm2, index_attack)
                index = random.randint(0, len(pkm2.attacks)-1)
                self.action(pkm2, pkm1, index)
            else:
                index = random.randint(0, len(pkm2.attacks)-1)
                self.action(pkm2, pkm1, index)
                self.action(pkm1, pkm2, index_attack)

        self.actual_turn += 1

    def is_finished(self):

        if self.pokemon1.current_HP <= 0:
            self.winner = self.pokemon2
            self.loser = self.pokemon1
        else:
            self.winner = self.pokemon1
            self.loser = self.pokemon2

        return self.pokemon1.current_HP <= 0 or self.pokemon2.current_HP <= 0

    def Calculation_EXP (self):

        e = self.loser.expbase
        c = self.typec
        l = self.loser.level

        if c == "s" :
            new_exp = (1*e*l)/7
        else :
            new_exp = (1.5*e*l)/7

        self.winner.xp = int(new_exp)
        print(self.winner.name)