import json

class Pokemon:
    def __init__(self, name=input("entrez le nom du nouveau pokémon :")):
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

    def register_pokemon(self):
        attribut = {
            "Name :": self.get_name(),
            "Health :": self.get_health(),
            "Level :": self.level,
            "Attack :": self.attack,
            "Defense :": self.defense,
            "Type :": self.type
        }
        pokemon_list = {
            "New pokemon": attribut
        }
        with open("pokemon_list", "r") as file:
            read_file = file.read()
            if self.get_name() in read_file:
                print("Pokémon déjà enregistré")
            else:
                with open("pokemon_list", "a+") as file:
                    json.dump(pokemon_list, file, indent=2)
                    print("pokémon enregistré")

#pokemon = Pokemon()
