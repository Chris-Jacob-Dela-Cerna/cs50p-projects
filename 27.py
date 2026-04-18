# Document: This python is my 3rd application of CS50P Week 4.

import requests

characters = requests.get("https://dragonball-api.com/api/characters?limit=58")
store = characters.json()

def main():
    start()

def start():
    userinput = input("System:   Enter 'characters' to see the list of characters.\nUsers:    ").strip().lower()
    if userinput == "characters":
        character_ui()
    else:
        pass

def character_ui():
    page = 0
    character_list(page)

def character_list(page):
    pages = 0
    pages += 10 * page

    print("\nList of Characters:")
    for eachid in range(10):
        print(eachid + 1, store["items"][pages + eachid].get("name"))
    print("")

main()