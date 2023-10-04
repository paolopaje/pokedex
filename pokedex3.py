import requests

def search_pokemon(name):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}/")
    if response.status_code != 200:
        print(f"Pokemon {name} not found.")
        return None

    pokemon = response.json()
    details = {
        "Name": pokemon["name"],
        "ID": pokemon["id"],
        "Moves": [move['move']['name'] for move in pokemon["moves"][:2]],
        "Held Items": [item['item']['name'] for item in pokemon["held_items"][:2]]
    }
    return details

if __name__ == "__main__":
    pokemon_names = set()
    pokemon_details = []
    i = 0
    while i < 6:
        pokemon_name = input(f"Enter the name of Pokemon {i+1}: ").lower()

        if pokemon_name in pokemon_names:
            print(f"You've already entered {pokemon_name}. Please enter a different Pokemon.")
            continue

        details = search_pokemon(pokemon_name)
        if details:
            pokemon_names.add(pokemon_name)
            pokemon_details.append(details)
            i += 1

    # Print the details for all unique Pokémon
    for details in pokemon_details:
        print("\nName", details["Name"])
        print("ID:", details["ID"])
        print("Moves:", ", ".join(details["Moves"]))
        print("Held Items:", ", ".join(details["Held Items"]))