import cgi
import http.cookies
#le module os permet de travailler sur tout ce qui est système d'exploitation
import os
import sys
import codecs

#modifier l'encodage pour la sortie standard
sys.stdout=codecs.getwriter("utf-8")(sys.stdout.detach())

#pour spécifier qu'on travaille sur le html
print("Content-type: text/html; charset-utf-8\n")

html="""<!DOCTYPE html>

<head>
    <meta charset="UTF-8">
    <title>Une page web avec python et HTML</title>
</head>
<body>
<h1>Cookies avec python</h1>
"""
print(html)
#lire les cookies (récupérer la variable d'environnement HTTP_COOKIE)
""" 
if "HTTP_COOKIE" in os.environ:
    print(os.environ["HTTP_COOKIE"])
else:
    print("HTTP_COOKIE n'existe pas")
"""
try:
    user_lang=http.cookies.SimpleCookie(os.environ["HTTP_COOKIE"])
    print(user_lang["langue"].value)
except(http.cookies.CookieError,KeyError):
    print("Non trouvé")

html=""" <p>il était une fois</p>
</body>
</html>
"""
print(html)
