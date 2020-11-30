#créer une liste pour stocker des pseudo pour simuler un jeu en ligne
online_players=["Graven", "Anana", "Cleymax","Bob"]
print(online_players)
print(online_players[0])
print(online_players[len(online_players)-1])
# modifier 'Graven' -->'Gravenilvec'
online_players[0]="Gravenilvec"
print(online_players[0])
#ajouter un elt à la liste
online_players.insert(2,"Bernard")
print(online_players)
#modifier plusieurs elts à la fois
online_players[2:4]=["Paul", "Jacques"]
print(online_players)
#en ajouter d'autres, on imagine qu'un joueur "Gameur123" se connecte, cmt l'ajouter à la fin de la liste
online_players.append("Gameur123")
print(online_players)
#ajouter plusieurs elts à la fin de la liste
online_players.extend(["Gogumerler", "Gigi"])
print(online_players)
#le joueur Anana se deconnecte
del online_players[1]
print(online_players)
#autre methode pour supprimer
online_players.pop(1)
print(online_players)
#autre methode pour la suppression par nom
online_players.remove("Bob")
print(online_players)
#supprimer tous les elts de la liste
online_players.clear()
print(online_players)