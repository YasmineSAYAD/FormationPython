
password=input("Entrer votre mot de passe: ")
# len permet de compter le nombre de caractères de la chaine en paramètres
password_length=len(password)
#verifier si le mot de passe est inférieure à  8 caractères
if password_length<=8:
    print("le mot de passe est trop court")
elif 8<password_length<12:
    print("mot de passe moyen")
else:
   print("Le mot de passe est valide")

print(password_length)