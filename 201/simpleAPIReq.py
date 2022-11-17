import requests # Run <<pip install requests>>
import time

while True:
    req = requests.get("https://kalob.io")
    print(req.status_code)
    time.sleep(5)