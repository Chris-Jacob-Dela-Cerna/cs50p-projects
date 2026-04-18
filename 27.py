# Document: This python is my 3rd application of CS50P Week 4.

import requests

characters = requests.get("https://dragonball-api.com/api/characters?limit=58")
store = characters.json()

def main():
    start()

def start():
    userinput = input("System:   Enter 'characters' to see the list of characters.\nUsers:    ").strip().lower()
    if userinput == "characters":
        character_list()
    else:
        pass

def character_list():
    print("\nList of Characters:")
    for eachid in range(len(store["items"])):
        print(eachid + 1, store["items"][eachid].get("name"))

main()