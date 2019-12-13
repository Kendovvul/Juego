import random
from constants import *

class Battle:

    def __init__(self, pkm1, pkm2, typec):
        self.pokemon1 = pkm1
        self.pokemon2 = pkm2
        self.actual_turn = 0
        self.typec = typec  ##char s : salvaje , e: entrenador
        self.winner = None
        self.loser = None
        self.Huir = False

    def Calculation_Damage(self, pkm1, pkm2, index_attack):
        Bonus = 1
        Effectiveness = EFFECTIVENESS[pkm1.attacks[index_attack].tipo[0]][pkm2.type1[1]] * EFFECTIVENESS[pkm1.attacks[index_attack].tipo[0]][pkm2.type2[1]]
        Varation = random.uniform(85, 100)
        Level = pkm1.level
        Power = pkm1.attacks[index_attack].power

        if pkm1.attacks[index_attack].category == PHYSICAL:
            Attack = pkm1.stats.Attack
            Defense = pkm2.stats.Defense

        elif pkm1.attacks[index_attack].category == SPECIAL:
            Attack = pkm1.stats.SpAttack
            Defense = pkm2.stats.SpDefense

        else:
            pass

        if (pkm1.attacks[index_attack].tipo == pkm1.type1[0] or pkm1.attacks[index_attack].tipo == pkm1.type2[0]):
            print(pkm1.attacks[index_attack].tipo)
            Bonus = 1.5


        damage = 0.01 * Bonus * Effectiveness * Varation * (((((0.2 * Level)+2) * Attack * Power)/(25 * Defense))+2)
        return int(damage)

    def action(self, pkm1, pkm2, index_attack):

        print(pkm1.name, "ha usado", pkm1.attacks[index_attack].name)

        if pkm1.attacks[index_attack].category == STATE:
            pass
        else:
            pkm2.current_HP -= self.Calculation_Damage(pkm1, pkm2, index_attack)
            pkm1.attacks[index_attack].Current_PP -= 1
        
        if pkm2.current_HP<=0:
            pkm2.current_HP = 0
            print(pkm2.name,":",str(pkm2.current_HP)+"/"+str(pkm2.Max_HP),"PS")
            return
        print(pkm2.name,":",str(pkm2.current_HP)+"/"+str(pkm2.Max_HP),"PS")

    def Combat(self):
        attacks = self.pokemon1.attacks
        cont = 0
        for x in attacks:
            print("("+str(cont)+")",x.name,str(x.Current_PP)+"/"+str(x.pp))
            cont+=1
        
        index_attack = int(input())
        while index_attack not in range(len(attacks)):
            index_attack = int(input())

        if self.pokemon1.stats.Speed > self.pokemon2.stats.Speed:
                self.action(self.pokemon1, self.pokemon2, index_attack)
                index = random.randint(0, len(self.pokemon2.attacks)-1)
                self.action(self.pokemon2, self.pokemon1, index)
        else:
            index = random.randint(0, len(self.pokemon2.attacks)-1)
            self.action(self.pokemon2, self.pokemon1, index)
            self.action(self.pokemon1, self.pokemon2, index_attack)

        self.actual_turn += 1

    def HUIR(self):
        self.Huir = True

    def Comando(self):
        print("¿Que deberia hacer", self.pokemon1.name+"?")
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
        if self.winner.name == self.pokemon1.name:
            print("Has ganado!!!")
            print("+",int(new_exp),"Exp")
        else:
            print("Tus pokemons se han debilitado")
            print("Has ido corriendo al centro pokemon mas cercano")