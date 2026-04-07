# # Document: This python is my 3rd application of CS50P Week 2.

''' This program will be used to note down different ways to use lists/dictionaries with the for loop.
The goal is to better understand the "for" loop. '''

# List for testing
fruits = ["apple", "banana", "orange"]

# List of Dictionaries for testing
fruitsncolor = [
    {"name": "apple", "color": "red"},
    {"name": "banana", "color": "yellow"},
    {"name": "orange", "color": "orange"}
]

# Nested Dictionaries for testing
fruitsncolor2 = {
    "apple": {"name": "apple", "color": "red"},
    "banana": {"name": "banana", "color": "yellow"},
    "orange": {"name": "orange", "color": "orange"}
}


for eachfruit in fruits:
    print(eachfruit)
print()

for eachfruit in fruitsncolor[2].keys():
    print(eachfruit)
print()

for eachfruit in fruitsncolor2["orange"].keys():
    print(eachfruit)