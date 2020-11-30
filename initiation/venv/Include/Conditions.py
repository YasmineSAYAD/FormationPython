# creer porte monnaie d'une personne
wallet=5000
#prix d un ordinateur
computer_price=2000

#verifier si le prix d'un ordinateur est inferieur a 1000£
#print(computer_price<1000)
#if computer_price < 1000 :
    #print("le prix de l'ordinateur est inférieur à 1000£")
#else:
   # print("Non, le prix est supérieur à 1000£")



 #if computer_price!=1000 :
    # print("Le prix n'est pas de 1000£")


# ou c'est or
if computer_price <= wallet and computer_price>1000 :
   print("l'achat est possible")
   # wallet = wallet-computer_price
    #print(str(wallet))
else:
    print("l'achat n'est pas possible")


 #autre façon pour ecrire les condition

  # text= ("L'achat est possible","L'achat est impossible")[computer_price<=1000]
  # print(text)
