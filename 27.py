# Document: This python is my 3rd application of CS50P Week 4.

import requests
import json

userartist = input("System:   Please enter an artist.\nUser:     ").strip().lower()

artist = requests.get(f"https://itunes.apple.com/search?entity=song&limit=50&term={userartist}")

print(json.dumps(artist.json(), indent=4))