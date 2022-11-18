import requests

while True:
    pokemonInput = input("Choose a Pokimon: ") #ditto
    pokemonInput = pokemonInput.lower()
    if pokemonInput == "stop":
        break
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemonInput}"

    req = requests.get(url)
    if req.status_code == 200:
        GetResponse = req.json()
        for ability in GetResponse['abilities']:
            getAbilityName = ability['ability']['name']
            print("Has an ability of", getAbilityName)
        # print("Has an ability of", GetResponse['abilities'][0]['ability']['name'])
        # print("Has an ability of", GetResponse['abilities'][1]['ability']['name'])
    else:
        print("Pokimon not found")