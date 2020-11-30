
user_admin="yasmine"


#fonction pour accéder à un profil d'un membre
def check_user(username):
    def decorator(func):
        def wrapper():
            if username==user_admin:
                return func()
            else:
                print("utilisateur inconnu")
        return wrapper
    return decorator
@check_user("yasmine") # c'est la même chose que profile=check_user("yasmine")(profile), (profile) est le paramètre de décorateur
def profile():
    print("Le profil membre...")

def page():
    """ page d'accès au profile"""
    print("Le profil membre...")

help(page) #si on utilise help pour une page décorée il va nous affiché la fonction décorateur et pas la fonction décorée
profile()