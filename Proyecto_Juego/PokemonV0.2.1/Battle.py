import random
from constants import *

class Battle:

    def __init__(self, pkm1, pkm2, typec):
        self.__Pokemon1 = pkm1
        self.__Pokemon2 = pkm2
        self.__Actual_Turn = 0
        self.__Type_Combat = typec  ##char s : salvaje , e: entrenador
        self.__Winner = None
        self.__Loser = None
        self.__Huir = False

    def Huir(self):
        return self.__Huir

    def ResetHuida(self):
        self.__Huir = False

    def Calculation_Damage(self, pkm1, pkm2, index_attack):
        Bonus = 1
        Effectiveness = EFFECTIVENESS[pkm1.getAttacks()[index_attack].getType()][pkm2.getType()[1]] * EFFECTIVENESS[pkm1.getAttacks()[index_attack].getType()][pkm2.getType()[1]]
        Varation = random.uniform(85, 100)
        Level = pkm1.getLevel()
        Power = pkm1.getAttacks()[index_attack].getPower()

        if pkm1.getAttacks()[index_attack].getCategory() == PHYSICAL:
            Attack = pkm1.getStats().getAttack()
            Defense = pkm2.getStats().getDefense()

        elif pkm1.getAttacks()[index_attack].getCategory() == SPECIAL:
            Attack = pkm1.getStats().getSpAttack()
            Defense = pkm2.getStats().getSpDefense()

        else:
            pass

        if (pkm1.getAttacks()[index_attack].getType() == pkm1.getType() or pkm1.getAttacks()[index_attack].getType() == pkm1.getType(False)):
            print(pkm1.getAttacks()[index_attack].getType())
            Bonus = 1.5


        damage = 0.01 * Bonus * Effectiveness * Varation * (((((0.2 * Level)+2) * Attack * Power)/(25 * Defense))+2)
        return int(damage)

    def action(self, pkm1, pkm2, index_attack):

        print(pkm1.getName(), "ha usado", pkm1.getAttacks()[index_attack].getName())

        if pkm1.getAttacks()[index_attack].getCategory() == STATE:
            pass

        else:
            pkm2.TakeDamage(self.Calculation_Damage(pkm1, pkm2, index_attack))
            pkm1.getAttacks()[index_attack].Attack()
        
        if pkm2.getCurrent_HP() <= 0:
            pkm2.setCurrent_HP(0)
            print(pkm2.getName(),":",str(pkm2.getCurrent_HP())+"/"+str(pkm2.getMax_HP()),"HP")
            return
        print(pkm2.getName(),":",str(pkm2.getCurrent_HP())+"/"+str(pkm2.getMax_HP()),"HP")

    def Combat(self):
        attacks = self.__Pokemon1.getAttacks()
        cont = 0

        for x in attacks:
            print("("+str(cont)+")",x.getName(),str(x.getCurrent_PP())+"/"+str(x.getPP()))
            cont+=1

        index_attack = int(input())

        while index_attack not in range(len(attacks)):
            index_attack = int(input())

        if self.__Pokemon1.getStats().getCurrent_Speed() > self.__Pokemon2.getStats().getCurrent_Speed():
                self.action(self.__Pokemon1, self.__Pokemon2, index_attack)
                index = random.randint(0, len(self.__Pokemon2.getAttacks())-1)
                self.action(self.__Pokemon2, self.__Pokemon1, index)
        else:
            index = random.randint(0, len(self.__Pokemon2.attacks)-1)
            self.action(self.__Pokemon2, self.__Pokemon1, index)
            self.action(self.__Pokemon1, self.__Pokemon2, index_attack)

        self.__Actual_Turn += 1

    def HUIR(self):
        self.__Huir = True

    def Comando(self):
        print("¿Que deberia hacer", self.__Pokemon1.getName()+"?")
        print("(1) LUCHA    (2) Mochila")
        print("(3) POKEMON  (4) HUIR")
        comando = input()
        while comando not in OPTIONS:

            comando = input()

        if comando == "1":
            self.Combat()
        elif comando == "2":
            #Mochila()
            pass
        elif comando == "3":
            pass
        else:
            self.HUIR()


    def is_finished(self):

        if self.__Pokemon1.getCurrent_HP() <= 0:
            self.__Winner = self.__Pokemon2
            self.__Loser = self.__Pokemon1
        else:
            self.__Winner = self.__Pokemon1
            self.__Loser = self.__Pokemon2

        return self.__Pokemon1.getCurrent_HP() <= 0 or self.__Pokemon2.getCurrent_HP() <= 0

    def Calculation_EXP (self):

        e = self.__Loser.getEXP_base()
        c = self.__Type_Combat
        l = self.__Loser.getLevel()

        if c == "s" :
            new_exp = (1*e*l)/7
        else :
            new_exp = (1.5*e*l)/7

        self.__Winner.AumentoDeEXP(int(new_exp))
        if self.__Winner.getName() == self.__Pokemon1.getName():
            print("Has ganado!!!")
            print("+",int(new_exp),"Exp")
            print("Nivel de experiencia ",int(new_exp),"/",self.__Winner.getExp_Next_Level())
            if self.__Winner.getEXP() >= self.__Winner.getExp_Next_Level():
                ##cambiar STATS D:
                self.__Winner.setExp_Next_Level(self.__Winner.Calculation_exp_lvl(self.__Winner.getGrow()))
                self.__Winner.SubirNevel()
                print(self.__Winner.getName()," ha subido de nivel")
                print("Nivel: ",self.__Winner.getLevel())

        else:
            print("Tus pokemons se han debilitado")
            print("Has ido corriendo al centro pokemon mas cercano")