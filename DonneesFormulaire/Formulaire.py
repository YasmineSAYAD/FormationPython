import cgi

#pour spécifier qu'on travaille sur le html
print("Content-type: text/html; charset-utf-8\n")
html="""<!DOCTYPE html>

<head>
    <meta charset="UTF-8">
    <title>Une page web avec python et HTML</title>
</head>
<body>
<h1>Page web en python</h1>
<form method="post" action="Result.py">
<p><input type="text" name="username">
 <input type="submit" name="Envoyer"></p>
</body>
</html>
"""
print(html)
