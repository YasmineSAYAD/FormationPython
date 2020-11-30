
"""
modes d'ouverture
r() lecture
w() ecriture avec remplacement
a() ecriture avec ajout en fin de fichier
x() lecture et ecriture
r+() lecture/ecriture dans un même fichier
"""
#Lecture

#enregistrer le fichier dans une variable et l'ouvrir
fic=open("fichier","r")

#lire un fichier
print(fic.read())

#lire une seule ligne
fic=open("fichier","r")
#les lignes dans un fichiers sont de type chaine de caracteres
nombre1=10
nombre2=fic.readline()
print(type(nombre2))
#il faut caster pour faire une addition par exemple
print(nombre1+int(nombre2))

#recuperer toutes les lignes qui restent
ligne=fic.readlines()
print(ligne)


try:
  fic.close()
  print("Le fichier est bien fermé")
except:
    print("erreur")

#autre mzthode pour ouvrir un fichier et le  fermer
with open("fichier","r") as fic:
     print(fic.read())
     #pas besoin de fermer le fichier avec with il se ferme automatiquement quand on sort de with

if fic.closed:
    print("Le fichier est bien fermé")

#ecriture
with open("fichier", "w") as fic:
    nombre=15
    fic.write(str(nombre))
    fic.write("\nBonjour")
    fic.write("\nBienvenue")
    fic.write("\n...\n")

