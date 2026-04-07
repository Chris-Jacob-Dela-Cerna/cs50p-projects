# # Document: This python is my 3rd application of CS50P Week 2.

''' This program will be used to note down different ways to use lists/dictionaries with the for loop.
The goal is to better understand the "for" loop. '''

''''''

# List for testing
fruits = ["apple", "banana", "orange"]

# For each value inside the list, it prints that value
for eachfruit in fruits:
    print(eachfruit)
print()

''''''

# List of Dictionaries for testing
fruitsncolor = [
    {"name": "apple", "color": "red"},
    {"name": "banana", "color": "yellow"},
    {"name": "orange", "color": "orange"}
]

# For each key inside the 3rd dictionary in the list, print that key
for eachkey in fruitsncolor[2].keys():
    print(eachkey)
print()

# For each value inside the 2nd dictionary, print that value
for eachvalue in fruitsncolor[1].values():
    print(eachvalue)
print()

# Update the 1st dictionary in the list by adding a new key and value
fruitsncolor[0].update({"flavor": "sweet"})
print(fruitsncolor)
print()

''''''

# Nested Dictionaries for testing
fruitsncolor2 = {
    "apple": {"name": "apple", "color": "red"},
    "banana": {"name": "banana", "color": "yellow"},
    "orange": {"name": "orange", "color": "orange"}
}

# For each key inside the "orange" dictionary in the dictionary, print that key
for eachfruit in fruitsncolor2["orange"].keys():
    print(eachfruit)
print()

# Get the value from the key "name" inside the "apple" dictionary in the dictionary, if no value print "No value". Otherwise, print the value
print(fruitsncolor2["apple"].get("name", "No value yet"))
print()

# Update the dictionary by adding a new key with a dictionary as a value 
fruitsncolor2.update({"grapes": {"name": "grapes", "color": "purple"}})
print(fruitsncolor2)
print()

''''''