import json
from normal import Normal


pokemon1 = Normal("Rattata")
pokemon2 = Normal("Miaouss")

pokemons = [pokemon1.save_pokemon(), pokemon2.save_pokemon()]

with open("pokemons_list.json", "w") as f:
    json.dump(pokemons, f, indent=2)