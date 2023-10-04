import requests
import sys

def search_pokemon(name):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}/")
    #response = requests.get("https://pokeapi.co/api/v2/pokemon/{}}".format{name})
    pokemon = response.json()
    print("Name: "+ str(pokemon["name"]))
    print("ID: "+ str(pokemon["id"]))
    print("Base_XP: "+ str(pokemon["base_experience"]))

if __name__ == "__main__":
    search_pokemon(sys.argv[1])