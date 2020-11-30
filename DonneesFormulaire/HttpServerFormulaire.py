import http.server


port=80
address=("",port) # "" veut dire que c'est local

server=http.server.HTTPServer

#gestionnaire de requetes http standard,il fonctionne avec l'interface de script CGI
handler=http.server.CGIHTTPRequestHandler

#spécifier un chemin où il va chercher, ["/"] c'est à dire à la racine
handler.cgi_directories=["/"]

#créer le serveur
httpd=server(address,handler)

print(f"Le serveur est démarré sur le port {port}")
# httpd.serve_forever() : pour que le serveur reste démarré jusqu'à ce qu'on quitte
httpd.serve_forever()
