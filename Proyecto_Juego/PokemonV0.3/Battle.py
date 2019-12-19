import random
from constants import *
from Combat import *

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
        self.__Turns = []

###############################################################################################################

    def addAction(self, action):
        self.__Turns.append(action)

###############################################################################################################

    def Huir(self):
        return self.__Huir

###############################################################################################################

    def ResetHuida(self):
        self.__Huir = False

###############################################################################################################

    def Command(self):
        comando = input()
        while comando not in OPTIONS:
            comando = input()
        return comando

###############################################################################################################

    def Combat(self, Pokemon):
        attacks = Pokemon.getAttacks()
        cont = 1

        for x in attacks:
            print("("+str(cont)+")",x.getName(),str(x.getCurrent_PP())+"/"+str(x.getPP()))
            cont+=1

        index_attack = int(input())-1

        while index_attack not in range(len(attacks)):
            index_attack = int(input())

        combat = Combat(Pokemon, index_attack)
        self.addAction(combat)


#################################################################################################################

    def Bag(self):
        bag = self.__Player.getBag()

        print("(1) Objetos  (2) Botiquin   (3) MT/MO")
        print("(4) Bayas    (5) OBJ. Clave")

        comando = str(input())

        while comando not in ["1","2","3","4","5"]:
            comando = str(input())

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

########################################################################################################

    def Chance_Pokemon(self):

        team = self.__Player.getTeam()
        cont = 1

        for pokemon in team:
            print("("+str(cont)+")", pokemon.getName())
            cont += 1

        pokemon_index = int(input())

        while pokemon_index not in range(len(team) + 1):
            pokemon_index = int(input())


        self.__Current_Pokemon = team[pokemon_index-1]


########################################################################################################

    def HUIR(self):
        self.__Huir = True

########################################################################################################

    def Comando(self):
        comando = input()
        while comando not in OPTIONS:
            comando = input()

        if comando == "1":
            print("---------Batalla---------")
            self.Combat(self.__Current_Pokemon)
        elif comando == "2":
            print("---------Mochila---------")
            self.Bag()
        elif comando == "3":
            print("---------Equipo---------")
            self.Chance_Pokemon()

        else:
            self.HUIR()

#########################################################################################################

    def bot(self):
        index_attack = random.randint(0, len(self.__Pokemon2.getAttacks()) - 1)
        combate = Combat(self.__Pokemon2, index_attack)
        combate.setFlag(flag = True)
        self.addAction(combate)

#########################################################################################################

    def Action(self):
        print("---------Menu---------")
        print("¿Que deberia hacer", self.__Current_Pokemon.getName()+"?")
        print("(1) LUCHA    (2) Mochila")
        print("(3) POKEMON  (4) HUIR")

        self.Comando()
        self.bot()
        
        for x in self.__Turns:
            if x.getFlag():
                x.setOpponent(self.__Pokemon2)
                x.Attack()
                if self.is_finished():
                    break
            else:
                x.setOpponent(self.__Current_Pokemon)
                x.Attack()
                if self.is_finished():
                    break

        self.__Turns.clear()

############################################################################################################

    def is_finished(self):

        if self.__Current_Pokemon.getCurrent_HP() <= 0:
            self.__Winner = self.__Pokemon2
            self.__Loser = self.__Current_Pokemon
        else:
            self.__Winner = self.__Current_Pokemon
            self.__Loser = self.__Pokemon2

        return self.__Current_Pokemon.getCurrent_HP() <= 0 or self.__Pokemon2.getCurrent_HP() <= 0

###############################################################################################################

    def Calculation_EXP (self):

        e = self.__Loser.getEXP_base()
        c = self.__Type_Combat
        l = self.__Loser.getLevel()

        if c == "s" :
            new_exp = (1*e*l)/7
        else :
            new_exp = (1.5*e*l)/7

        self.__Winner.AumentoDeEXP(int(new_exp))
        if self.__Winner.getName() == self.__Current_Pokemon.getName():
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