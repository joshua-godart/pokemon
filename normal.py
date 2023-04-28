from pokemon import Pokemon

class Normal(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.__health = 100
        self.level = 1
        self.attack = 5
        self.defense = 0
        self.type = "Normal"

normal = Normal("Evoli")
normal.add_pokemon()

