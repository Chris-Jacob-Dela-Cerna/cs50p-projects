# Document: This python is my 3rd application of CS50P Week 4.

import requests

characters = requests.get("https://dragonball-api.com/api/characters?limit=58")
api = characters.json()

idlist = []
for number in range(58):
    idlist.append(str(number))

character_keys = ["name", "ki", "maxKi", "race", "gender", "affiliation"]



def start():
    while True:
        userinput = input("\nSystem:   Enter a characterid to see their info.\n          Enter 'characters' to see the list of characterids.\nUsers:    ").strip().lower()
        if userinput == "characters":
            character_ui()
        else:
            if userinput in idlist:
                selected_character(int(userinput) - 1)
                break
            else:
                print(f"System:   characterid [{userinput}] is invalid.")

def character_ui():
    userpage = 0
    while True:
        uipage = userpage + 1
        if 0 <= userpage <= 5:
            character_list(userpage)
            try:
                userpage = int(input(f"Current page: {uipage}/6\n>>> ").strip())
            except ValueError:
                continue
            except EOFError:
                break
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

def selected_character(id):
    for eachkey in character_keys:
        print(f" | {eachkey.title()}: {api["items"][id].get(eachkey)}")

start()