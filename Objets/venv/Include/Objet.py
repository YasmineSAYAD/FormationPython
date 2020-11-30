from  model.Player import Player
from  model.Weapon import Weapon

knife=Weapon("Couteau",3)

player1=Player("Graven",20,3)
player2=Player("Bob",20,5)
player1.attaque_player(player2)
print(player1.get_pseudo()," attaque ",player2.get_pseudo())


print("Bienvenue au joueur",player1.get_pseudo() , " / Points de vie", player1.get_health(), " / Attaques", player1.get_attaque())
print("Bienvenue au joueur", player2.get_pseudo(), " / Points de vie", player2.get_health(), " / Attaques", player2.get_attaque())



