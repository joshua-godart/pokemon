from pokemon import Pokemon

class Normal(Pokemon):
    def __init__(self, name=input("entrez le nom du nouveau pokémon :")):
        super().__init__(name)
        self.__health = 100
        self.level = 1
        self.attack = 5
        self.defense = 0
        self.type = "Normal"
    #def attack_elements(self):
        #if Combat.enemy_choice() == self.type:
            #self.attack = self.attack*1
        #else:
            #self.attack = self.attack*0.75


normal = Normal()
normal.register_pokemon()

