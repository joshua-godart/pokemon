import json
import random
from pokemon import Pokemon
class Combat:
    def __init__(self):
        pass

    def pokemon_choice(self):
        with open("pokedex.json", "r") as file:
            pokemon_list = json.load(file)
        pokemon = random.choice(pokemon_list)
        print(pokemon)
    def enemy_choice(self):
        with open("pokemons_list.json", "r") as file:
            pokemon_list = json.load(file)
        enemy = random.choice(pokemon_list)
        print(enemy)
        print(enemy["Type :"])

    def get_type_enemy(self):
        pass
    def start_fight(self):
        pass

combat= Combat()
combat.enemy_choice()
combat.pokemon_choice()