import cgi
import cgitb
#cgitb pour le débugage et gérer les cgi pour traiter les données du formulaire

#activer le mode débug
cgitb.enable()
#recuperer les informations transmises
form=cgi.FieldStorage()

#La partie html

#pour spécifier qu'on travaille sur le html
print("Content-type: text/html; charset-utf-8\n")
html="""<!DOCTYPE html>

<head>
    <meta charset="UTF-8">
    <title>Page de résultat</title>
</head>
<body>

"""
print("<h1>Page de résultats</h1>")
#verifier si le champ existe existe
try:
    if form.getvalue("username"):
       username=form.getvalue("username")
       print(f"<p>Bonjour {username}</p>")
       #pour securiser
       print("<script>alert('Vous acceptez de recevoir les données?')</script>")
    else:
        raise Exception("Pseudo non transmis")
except:
    print("<p>Pseudo non transmis</p>")



print(html)

html="""

</body>
</html>
"""
print(html)