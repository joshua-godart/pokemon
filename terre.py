from pokemon import Pokemon
from combat import Combat
class Terre(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.__health = 120
        self.level = 1
        self.attack = 5
        self.defense = 5
        self.type = "Terre"