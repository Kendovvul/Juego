from pkm import *
#from constants import *

#STATS

pkm1_stats = Stats(45,60,40,70,50,54) #HP, Attack, Defense, SpAttack, SpDefense, Speed
pkm2_stats = Stats(40,45,30,65,55,70) #HP, Attack, Defense, SpAttack, SpDefense, Speed


#POKEMONS

pkm1 = Pokemon("Torchic", "fire", None, pkm1_stats, 5, 65)  ##nombre, tipo1, tipo2, nivel
pkm2 = Pokemon("Treecko", "plant", None, pkm2_stats, 5, 65)

print(int(pkm1.Max_HP))
print(int(pkm2.Max_HP))

#ATTACKS
pkm1.attacks = [Attack("Arañazo","normal","fisico",35,40,100)]
pkm2.attacks = [Attack("Arañazo","normal","fisico",35,40,100)]



#BATTLE

batalla = Battle(pkm1, pkm2, "s")

while not batalla.is_finished():

	batalla.combat(batalla.pokemon1, batalla.pokemon2)

print("El combate a finalizado")


batalla.Calculation_EXP()