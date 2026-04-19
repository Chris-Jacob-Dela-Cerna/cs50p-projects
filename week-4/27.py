# Document: This python is my 3rd application of CS50P Week 4.

import requests

characters = requests.get("https://dragonball-api.com/api/characters?limit=58")
api = characters.json()

def main():
    start()

def start():
    userinput = input("System:   Enter 'characters' to see the list of characters.\nUsers:    ").strip().lower()
    if userinput == "characters":
        character_ui()
    else:
        pass

def character_ui():
    userpage = 0
    while True:
        character_list(userpage)
        userpage = int(input("\nSystem:   Enter a page.\nUser:     ").strip())

def character_list(userpage):
    page = 10 * userpage

    print("\nList of Characters:")
    for number in range(10):
        id = page + number
        if id < 58:
            print(id + 1, api["items"][id].get("name"))

main()