from pokemon import Pokemon
from combat import Combat
class Feu(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.__health = 100
        self.level = 1
        self.attack = 8
        self.defense = 0
        self.type = "Feu"

    def calcul_attack(self):
        enemy = Combat.enemy_choice(self)
        type = enemy["Type"]
        print(type)

        if type == "Eau":
            self.attack = self.attack * 0.5
            print(self.attack)
        elif type == "Terre":
            self.attack = self.attack * 2
            print(self.attack)
        else:
            self.attack = self.attack * 1
            print(self.attack)

feu = Feu("Goupix")
feu.calcul_attack()