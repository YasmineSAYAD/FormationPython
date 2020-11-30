import pickle

class Player:
    def __init__(self,name,level):
        self.name=name
        self.level=level

    def afficher(self):
         print("{} ({})".format(self.name,self.level))

p1=Player("Jeason",10)
p1.afficher()

#enregistrer les infos d'un joueurs dans un fichier en utilisant le module pickle
#wb w:ecriture b:en binaire // wt t:text
with open("player.data","wb") as fichierPlayer:
    #creer une variable qui sert à l'enregistrement
     record=pickle.Pickler(fichierPlayer)
    #copier les infos sur l'objet créé
     record.dump(p1)

#verifier si le fichier a été bien créé
with open("player.data","rb") as fichierPlayer:
    get_record=pickle.Unpickler(fichierPlayer)
    player_rec=get_record.load()
    player_rec.afficher()