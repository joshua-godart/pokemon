import json
import random
class Combat:
    def __init__(self):
        pass

    def pokemon_choice(self):
        with open("pokedex.json", "r") as file:
            pokemon_list = json.load(file)
        return random.choice(pokemon_list)
        #print(pokemon)
        #print(pokemon["Type"])
    def enemy_choice(self):
        with open("pokemons_list.json", "r") as file:
            pokemon_list = json.load(file)
        return random.choice(pokemon_list)
        #print(enemy)
        #print(enemy["Type"])

    def get_type_enemy(self):
        pass
    def start_fight(self):
        pokemon1 = self.pokemon_choice()
        attack1 = pokemon1["Attack"]
        print(pokemon1["Name"], attack1)

        pokemon2 = self.enemy_choice()
        attack2 = pokemon2["Attack"]
        print(pokemon2["Name"], attack2)




combat = Combat()
combat.pokemon_choice()
combat.enemy_choice()
combat.start_fight()
