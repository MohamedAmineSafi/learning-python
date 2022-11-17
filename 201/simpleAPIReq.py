import requests # Run <<pip install requests>>

req = requests.get("https://kalob.io")
print(req.status_code)