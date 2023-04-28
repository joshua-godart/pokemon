import json

class Pokemon:
    def __init__(self, name):
        self.__name = name
        self.__health = 100
        self.level = 1
        self.attack = 5
        self.defense = 0
        self.type = ""

    def get_name(self):
        return self.__name
    def get_health(self):
        return self.__health

    def get_type(self):
        return self.type
    def pokemon_infos(self):
        print("Nom :", self.get_name())
        print("Santé :", self.get_health())
        print("Niveau :", self.level)
        print("Attaque :", self.attack)
        print("Défense :", self.defense)
        print("Type :", self.type)

    def save_pokemon(self):
        return {
            "Name :": self.get_name(),
            "Health :": self.get_health(),
            "Level :": self.level,
            "Attack :": self.attack,
            "Defense :": self.defense,
            "Type :": self.get_type()
        }

    def add_pokemon(self):
        with open('pokemons_list.json', 'r') as f:
            pokemon_list = json.load(f)
            new_pokemon = self.save_pokemon()
            pokemon_list.append(new_pokemon)
        with open('pokemons_list.json', 'w') as f:
            json.dump(pokemon_list, f, indent=2)

#pokemon = Pokemon()
