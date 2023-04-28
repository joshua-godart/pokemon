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
        #enemy = Combat.enemy_choice()
        #print(enemy["Type :"])
        pass

normal = Normal("Evoli")
normal.calcul_attack()

