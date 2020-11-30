import cgi
#pour spécifier qu'on travaille sur le html
print("Content-type: text/html; charset-utf-8\n")
html="""<!DOCTYPE html>

<head>
    <meta charset="UTF-8">
    <title>Une page web avec python et HTML</title>
</head>
<body>
<h1>Bienvenue</h1>
<p>Je suis en python, avec une page web HTML</p>
</body>
</html>
"""
print(html)
