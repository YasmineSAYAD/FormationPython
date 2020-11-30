import time

print("Bonjouuur")
time.sleep(3)
print("Bienvenue")

#gestion de temps
"""
1 er janvier 1970 à 00h00 c'est la date de depart choisie en informatique, 
c'est à dire à partir de cette date on commence à calculer le nombre de secondes jusqu'à ce jour
cette était choisie par rapport à l'informatique qui est popularisé en cette date
"""
#compter le nombre de seconde de la date de départ jusqu'à cette seconde
print(time.time())

#exemple
begin=time.time()
print("Debut")
time.sleep(3)
end=time.time()
print("Fin")
print(f"Temps d'execution: {end-begin} s")

#elle se base sur le même principe que time.time() si on précise pas de paramètres
tps=time.localtime()
print(tps)
#convertir tps en temps standard
print(time.mktime(tps))

"""
%d :jour(01 à 31)
%m :mois(01 à 12)
%Y :année(exemple:2018)
%H :heure(00 à 24)
%I :minute(00 à 59)
%S :seconde(00 à 59)
%p :AM/PM
%A :jour de la semaine
%a :jour abrégé
%B :mois (nom du mois)
%b :mois abrégé
%Z :fuseau horaire (timezone)
"""
#une chaine pour manipuler du temps
print(time.strftime("%A"))
print(time.strftime("%Z"))