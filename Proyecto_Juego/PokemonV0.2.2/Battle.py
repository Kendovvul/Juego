import random
from constants import *

class Battle:

    def __init__(self, player, pkm2, typec):
        self.__Player = player
        self.__Current_Pokemon = player.getTeam()[0]
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

    def Command(self):
        comando = input()
        while comando not in OPTIONS:
            comando = input()
        return comando

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

    def Attack(self, pkm1, pkm2, index_attack):

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


###############################################################################################################
    def Combat(self):
        Pokemon1 = self.__Current_Pokemon
        attacks = Pokemon1.getAttacks()
        cont = 1

        for x in attacks:
            print("("+str(cont)+")",x.getName(),str(x.getCurrent_PP())+"/"+str(x.getPP()))
            cont+=1

        index_attack = int(input())-1

        while index_attack not in range(len(attacks)):
            index_attack = int(input())

        if Pokemon1.getStats().getCurrent_Speed() > self.__Pokemon2.getStats().getCurrent_Speed():
                self.Attack(Pokemon1, self.__Pokemon2, index_attack)
                index = random.randint(0, len(self.__Pokemon2.getAttacks())-1)
                self.Attack(self.__Pokemon2, Pokemon1, index)
        else:
            index = random.randint(0, len(self.__Pokemon2.attacks)-1)
            self.Attack(self.__Pokemon2, Pokemon1, index)
            self.Attack(Pokemon1, self.__Pokemon2, index_attack)

        self.__Actual_Turn += 1
#################################################################################################################}


    def Bag(self):
        bag = self.__Player.getBag()

        print("(1) Objetos  (2) Botiquin   (3) MT/MO")
        print("(4) Bayas    (5) OBJ. Clave")

        comando = str(input())

        while comando not in ["1","2","3","4","5"]:
            comando = input()

        if(comando == "1"):
            print("---------Objetos---------")
            pass
        elif(comando == "2"):
            print("---------Botiquin---------")
            bag.Botiquin(self.__Player.getTeam())
        elif(comando == "3"):
            print("---------MT/MO---------")
            pass
        elif(comando == "4"):
            print("---------Bayas---------")
            pass
        else:
            print("---------OBJ. Clave---------")
            pass


    def HUIR(self):
        self.__Huir = True

    def Comando(self):
        print("---------Menu---------")
        print("¿Que deberia hacer", self.__Player.getTeam()[0].getName()+"?")
        print("(1) LUCHA    (2) Mochila")
        print("(3) POKEMON  (4) HUIR")
        comando = input()

        index_pokemon = 0
        while comando not in OPTIONS:
            comando = input()

        if comando == "1":
            print("---------Batalla---------")
            self.Combat()
        elif comando == "2":
            print("---------Mochila---------")
            self.Bag()
            pass
        elif comando == "3":
            print("---------Equipo---------")
            pass
        else:
            self.HUIR()


    def is_finished(self):

        if self.__Current_Pokemon.getCurrent_HP() <= 0:
            self.__Winner = self.__Pokemon2
            self.__Loser = self.__Current_Pokemon
        else:
            self.__Winner = self.__Current_Pokemon
            self.__Loser = self.__Pokemon2

        return self.__Current_Pokemon.getCurrent_HP() <= 0 or self.__Pokemon2.getCurrent_HP() <= 0

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