class  Player:
    #constructeur
    def __init__(self,pseudo,health,attaque):
        self.pseudo=pseudo
        self.health=health
        self.attaque=attaque
        self.weapon=None
        print("Bienvenue au joueur",pseudo," / Points de vie",health," / Attaques",attaque)

    def get_pseudo(self):
        return self.pseudo

    def get_health(self):
        return self.health

    def get_attaque(self):
        return self.attaque

    def damage(self,damage):
        self.health-=damage
        print("Aie...Vous venez de subir ",damage," dégats!")

    def attaque_player(self,target_player):
        target_player.damage(self.attaque)