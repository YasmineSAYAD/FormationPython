#un tuple est constant on peut pas le modifier mais on peut effectuer une affectation multiple
#creer un tuple
# un tuple à une seule valeur mon_tuple = (40,)
#un tuple à plusieurs valeurs
mon_tuple = (40,45)
print(type(mon_tuple))
#acceder un element dans un tuple
try:
  print(mon_tuple[1])
except:
  print("longueur dépassée")

#utilité d'un tuple
(nombre1,nombre2)=(14,17)
print(nombre1)
print(nombre2)

#affectation multiple
nombre1=15
print(nombre1)
"""
2 raisons d'utiliser les tuples: affectation multiple de valeurs
                                 retour multiple de fonctions
"""
def get_player_position():
    posex=148
    posy=86
    return (posex,posy)

#programme principale
coordx=0
coordy=0
print("position du joueur :({}/{})".format(coordx,coordy))
(coordx,coordy)=get_player_position()
print("position du joueur :({}/{})".format(coordx,coordy))