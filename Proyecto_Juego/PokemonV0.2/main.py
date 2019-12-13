from constants import *
from Pokemon import *
from Battle import *
from Attack import *
from Stats import *

#STATS
print(PHYSICAL)

pkm1_stats = Stats(45,60,40,70,50,54) #HP, Attack, Defense, SpAttack, SpDefense, Speed
pkm2_stats = Stats(40,45,30,65,55,70) #HP, Attack, Defense, SpAttack, SpDefense, Speed


#POKEMONS

pkm1 = Pokemon("Treecko", Grass, NONE, pkm2_stats, 5, 65)
pkm2 = Pokemon("Torchic", Fire, NONE, pkm1_stats, 5, 65)  ##nombre, tipo1, tipo2, nivel


#ATTACKS
pkm1.attacks = [Attack("Destructor",Normal,PHYSICAL,35,40,100), Attack("Malicioso", Normal, STATE, 30, 0, 100)]
pkm2.attacks = [Attack("Arañazo"   ,Normal,PHYSICAL,35,40,100), Attack("Gruñido",   Normal, STATE, 40, 0, 100)]



#BATTLE

batalla = Battle(pkm1, pkm2, "s")

while not batalla.Huir and not batalla.is_finished():

	batalla.Comando()
	##batalla.combat(batalla.pokemon1, batalla.pokemon2)

print("El combate a finalizado")

if batalla.Huir == False:
	batalla.Calculation_EXP()
else:
	print("Has huido")
	batalla.huir = False