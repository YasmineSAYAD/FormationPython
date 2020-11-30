import cgi
import http.cookies
import datetime


#expires: date d'expiration
#path
#comment: faire des commentaires sur le cookie
#domain: domaine de site
#max-age:la duréé du cookie ça ne fonctionne pas sur tout les navigateurs
#secure: si le cookie fonctionne sur une connexion https (sécurisée)
#version
#httponly: empêcher que le cookie soit exploitable depuis javascript, pour éviter su'un code java script peut recupérer le cookie
#httponly et secure on les met seule , les autres on leur affecte des valeurs
#Set-Cookie: username=yasmine;secure;httponly;


#l'entête du cookie, il faut le génerer avant le code html sinon ça ne marchera pas
#print("Set-Cookie: langue=fr;httponly;")
#mais dans notre exemple on va utiliser un module python

#date d'expiration une année
expiration=datetime.datetime.now()+datetime.timedelta(days=365)

#formater la date
expiration=expiration.strftime("%a,%d-%b-%Y %H:%M:%S")
#génerer et créer un cookie
my_cookie=http.cookies.SimpleCookie()
my_cookie["langue"]="Kabyle"
my_cookie["langue"]["expires"]=expiration
my_cookie["langue"]["httponly"]=True
print(my_cookie.output())

#pour spécifier qu'on travaille sur le html
print("Content-type: text/html; charset-utf-8\n")

html="""<!DOCTYPE html>

<head>
    <meta charset="UTF-8">
    <title>Une page web avec python et HTML</title>
</head>
<body>
<h1>Cookies avec python</h1>
<p>Bonjour</p>
</body>
</html>
"""
print(html)
