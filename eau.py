from pokemon import Pokemon

class Eau(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.__health = 100
        self.level = 1
        self.attack = 7
        self.defense = 3
        self.type = "Eau"

eau = Eau("Carapuce")
