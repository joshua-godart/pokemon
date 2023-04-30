from pokemon import Pokemon
from combat import Combat
class Eau(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.__health = 100
        self.level = 1
        self.attack = 7
        self.defense = 3
        self.type = "Eau"

    def calcul_attack(self):
        enemy = Combat.enemy_choice(self)
        type = enemy["Type"]
        print(type)

        if type == "Terre":
            self.attack = self.attack * 0.5
            print(self.attack)
        elif type == "Feu":
            self.attack = self.attack * 2
            print(self.attack)
        else:
            self.attack = self.attack * 1
            print(self.attack)

eau = Eau("Carapuce")
eau.calcul_attack()
