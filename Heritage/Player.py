class  Player:
    #constructeur
    def __init__(self,pseudo,health,attaque):
        self.pseudo=pseudo
        self.health=health
        self.attaque=attaque
        
        print("Bienvenue au guerrier",pseudo," / Points de vie",health," / Attaques",attaque)

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



player1=Player("Graven",20,3)
player1.damage(3)


#pour l'heritage multiple exemole Warrior(Player,Classe2)
class Warrior(Player):
    # constructeur
    def __init__(self,pseudo,health,attaque):
        super().__init__(pseudo,health,attaque)
        self.armor = 3
        print("Bienvenue au guerrier", pseudo, " / Points de vie", health, " / Attaques", attaque)

    def damage(self, damage):
        #si ya pas de code et on veut pas d'erreur on utilise pass
        if self.armor>0:
            self.armor-=1
            damage=0
        super().damage(damage)

    def blade(self):
        self.armor = 3
        print("les points d'armure ont été rechargés")

    # renvoyer le nombre de points d'armure que possède le guerrier
    def get_armor_point(self):
       return self.armor


player1 = Player("Graven", 20, 3)
player1.damage(3)

warrior = Warrior("Dark warrior", 30, 2)
# nombre de dégats
warrior.damage(4)
print("Vie: ", warrior.get_health(), "/ armure: ", warrior.get_armor_point())

#tester si l'heritage est bien fait
if issubclass(Warrior,Player):
    print("Le guerrier est bien une spécialisation du player")