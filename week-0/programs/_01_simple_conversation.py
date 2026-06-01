# Document: This python is my 1st application of CS50P Week 0

# Asks the user's name. Remove whitespace from str and capitalize name
name = input("Who are you? ").strip().title()

# Says Hello to the user
print("Hello, " + name)

# Ask the user's age
age = input("How about your age? ")
print(f"At {age}, you can still make it!")

# Asks what's the user's favorite color
color = input("What's your \"favorite\" color then? ").strip().lower()
print(color, "?", sep="", end=" ")
print("that's a fantastic color!")

# Asks the user a flag related to that color
print(f"Can you think of a flag with {color} as one of its colors?")