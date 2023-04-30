from pokemon import Pokemon
from combat import Combat
class Terre(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.__health = 100
        self.level = 1
        self.attack = 5
        self.defense = 5
        self.type = "Terre"

    def calcul_attack(self):
        enemy = Combat.enemy_choice(self)
        type = enemy["Type"]
        print(type)

        if type == "Feu":
            self.attack = self.attack * 0.5
            print(self.attack)
        elif type == "Eau":
            self.attack = self.attack * 2
            print(self.attack)
        else:
            self.attack = self.attack * 1
            print(self.attack)

terre = Terre("Sabelette")
terre.calcul_attack()
