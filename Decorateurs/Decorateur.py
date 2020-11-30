#un décorateur permet d'etendre les fonctionalités et changer un comportement
"""
notation d'un décorateur:
 func=decorator(func)
 ou
@decorator on  le met avant la fonction qu'on va décorer
"""

""" 
def decorator(func):
    print("------------------")
    return func

def hello():
    print("Hello")

hello=decorator(hello)
hello()
"""
""" 
#le type des fonction et des methodes en python est:collable
def decorator(func):
    print("------------------")
    return func

@decorator
def hello():
    print("Hello")

hello()
print(type(hello))
"""

#fonction pour accéder à un profil d'un membre
def decorator(func):
    def wrapper():
        if user_logged:
            return func()
        else:
            print("vous devez être connecté")
    return wrapper
user_logged=True
@decorator
def profile():
    print("Le profil membre...")

@decorator
def article():
    print("La page des articles...")
article()
profile()