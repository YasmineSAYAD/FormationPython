#creation d'un dictionnaire
dico={1:"one","mouse":"souris","dog":"chien","hello":"salut"}
print(dico["mouse"])
print(dico[1])

#ajout
dico[2]="two"
print(dico)

#modification
dico[2]="deux"
print(dico)

#suppression
dico.pop("dog")
print(dico)

#recuperer la valeur supprimée
valeur_supprimee=dico.pop(1)
print(valeur_supprimee)

#autre methode pour supprimer
del dico[2]
print(dico)

#verifier l'existence d'une clé
print("mouse" in dico)

#recuperer les clés
for key in dico.keys():
 print(key)

# recuperer les clés et leurs valeurs
for key,valeur in dico.items():
    print("Clé : {} - valeur : {}".format(key,valeur))

#créer une copie d'un dictionnaire
dico2=dico.copy()
print(dico2)
print(dico)
dico["ok"]="ok"
print(dico2)
print(dico)

#fonction avec des parametres nommés
#** paramètres obligatoirement nommés
#* paramètres variables
def fonctionParametre(**parametres):
    print(parametres)

fonctionParametre(p=12,a="ok")


