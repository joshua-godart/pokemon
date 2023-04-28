from pokemon import Pokemon
from combat import Combat

class Normal(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.__health = 100
        self.level = 1
        self.attack = 5
        self.defense = 0
        self.type = "Normal"


    def calcul_attack(self):
        enemy = Combat.enemy_choice(self)
        type = enemy["Type"]
        print(type)
        if type == self.get_type():
            self.attack = self.attack
            print(self.attack)
        else:
            self.attack = self.attack * 0.75
            print(self.attack)

normal = Normal("Evoli")
print(normal.calcul_attack())

