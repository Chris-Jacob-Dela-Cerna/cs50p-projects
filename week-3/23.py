# Document: This python is my 2nd application of CS50P Week 3.

fruits = [
    "apple",
    "banana",
    "orange",
    "strawberry",
    "grapes",
    "watermelon",
    "guava",
    "papaya",
    "dragonfruit",
    "avocado"
]

print("\nHere are the list of fruits, only one is the winner:")
base = 0
for eachfruit in fruits:
    base += 1
    print(f"{base}. {eachfruit} ")

userfruit = input("User: ").strip().lower()

if userfruit in fruits:
    if userfruit == fruits[5]:
        print("We have a winner!")
    else:
        print("Better luck next time.")
else:
    raise ValueError(f"{userfruit.title()} is not in the list.")