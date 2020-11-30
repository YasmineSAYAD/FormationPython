from statistics import mean
from random import shuffle
#jouer à la maitresse
notes=[8, 12, 10, 9, 4, 20, 14, 3]
print(notes)
#module: statistics

result=mean(notes)
print("la moyenne de l'élève est de {} ".format(result))

#module random
shuffle(notes)
print(notes)

# creer une liste
text=input("Entrer une chaine de la forme(email-pseudo-motdepasse)").split("-")
#split() pour décoper une chaine par un délimiteur
print(text)
print("salut {}, ton email {}, ton mot de passe {}".format(text[1], text[0], text[2]))
