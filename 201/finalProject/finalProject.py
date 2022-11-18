import requests

# pokemonInput = input("Choose a Pokimon: ") #ditto
# url = f"https://pokeapi.co/api/v2/pokemon/{pokemonInput}"
url = f"https://pokeapi.co/api/v2/pokemon/ditto"

req = requests.get(url)
GetResponse = req.json()
print("Has an ability of", GetResponse['abilities'][0]['ability']['name'])
print("Has an ability of", GetResponse['abilities'][1]['ability']['name'])