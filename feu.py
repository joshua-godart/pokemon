from pokemon import Pokemon
class Feu(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.__health = 100
        self.level = 1
        self.attack = 8
        self.defense = 0
        self.type = "Feu"

feu = Feu("Goupix")
feu.add_pokemon()