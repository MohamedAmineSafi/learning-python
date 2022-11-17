import requests # Run <<pip install requests>>

req = requests.get("https://swapi.dev/api/people/1")
person = req.json()

print(f'{person["name"]} is present in these films:')
for filmURL in person["films"]:
    req = requests.get(filmURL)
    filmData = req.json()
    print(f"\t {filmData['title']}")