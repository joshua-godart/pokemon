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

    def start_fight(self):
        pokemon1 = self.pokemon_choice()
        type1 = pokemon1["Type"]
        pokemon2 = self.enemy_choice()
        type2 = pokemon2["Type"]


        print(f"un combat débute entre", pokemon1["Name"], "et", pokemon2["Name"])

        while pokemon1["Health"] > 0 and pokemon2["Health"] > 0:
            succeed_list = [0, 1]
            succeed = random.choice(succeed_list)

            if pokemon2["Health"] >= pokemon1["Attack"]:
                if succeed == 1:
                    pokemon2["Health"] -= pokemon1["Attack"]
                    print(f"{pokemon1['Name']} inflige {pokemon1['Attack']} à "
                          f"{pokemon2['Name']}, il lui reste {pokemon2['Health']}")
                else:
                    pokemon2["Health"] -= 0
                    print(f"L'attaque de {pokemon1['Name']} a échoué !")
            else:
                print(f"{pokemon2['Name']} ennemi a perdu !")
                break


            if pokemon1["Health"] >= pokemon2["Attack"]:
                if succeed == 1:
                    pokemon1["Health"] -= pokemon2["Attack"]
                    print(f"{pokemon2['Name']} inflige {pokemon2['Attack']} à "
                          f"{pokemon1['Name']}, il lui reste {pokemon1['Health']}")
                else:
                    pokemon1["Health"] -= 0
                    print(f"L'attaque de {pokemon2['Name']} a échoué !")
            else:
                print(f"{pokemon1['Name']} joueur a perdu !")
                break








combat = Combat()
combat.pokemon_choice()
combat.enemy_choice()
combat.start_fight()
