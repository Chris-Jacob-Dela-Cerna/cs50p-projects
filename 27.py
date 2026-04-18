# Document: This python is my 3rd application of CS50P Week 4.

import requests


characters = requests.get("https://dragonball-api.com/api/characters")

store = characters.json()

for eachid in range(len(store["items"])):
    print(eachid + 1, store["items"][eachid].get("name"))