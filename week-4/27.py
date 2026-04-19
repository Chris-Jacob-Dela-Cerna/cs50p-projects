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
        uipage = userpage + 1
        if 0 <= userpage < 6:
            character_list(userpage)
            try:
                userpage = int(input(f"Current page: {uipage}/6\n>>> ").strip())
            except ValueError:
                continue
            else:
                userpage = userpage - 1
        else:
            userpage = 0

def character_list(userpage):
    print("\nList of Characters:")
    page = 10 * userpage
    for number in range(10):
        id = page + number
        if id < 58:
            print(id + 1, api["items"][id].get("name"))

main()