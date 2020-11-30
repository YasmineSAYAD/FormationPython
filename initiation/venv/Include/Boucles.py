for num_client in range(1,5):
 print("Vous êtes le client N°", num_client)

#for each : pour chaque valeur d'une liste donnée
 emails=["sayad@gmail.com", "yasmine@gmail.com", "abc@yahoo.fr","gravendev@gmail.com"," steelaxiss@free.fr"]
# for email in emails:
    # print("Email envoyé à", email)
 #blacklist
 blacklist=["gravendev@gmail.com"," steelaxiss@free.fr" ]
 for email in  emails:
     if email in blacklist:
         print("Email {} interdit ! envoi impossible..." .format(email))
         continue
 print("Email envoyé à", email)

#while
#salarié 1500£/mois
salary=1500
#tq salaire<2000,+120£
while salary<2000:
    salary+=120
    print("Votre salaire actuel est de ",salary,"£")
print("fin du programme")

#un youtubeur a 2500 abonnées
suscribers_count=2500
#il gagne 10% d'audience supplimentaire par mois
months=0
#estimer combien gagnera t'il d'abonnées après 2 ans
while months<=24:
    #augmenter l'audience
    suscribers_count*=1.10
    print("Vous avez actuellement {} abonnées !".format(suscribers_count))
    #on passe au mois suivant
    months+=1