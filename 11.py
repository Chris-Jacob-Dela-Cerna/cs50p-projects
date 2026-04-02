# Document: This python is my last application of CS50P Week 0.

# Greets user
def greet():
    print()
    print("Greetings user. ")

# Prompts user for text and mass value
def insert():
    name = input("Enter text: ").strip().lower()
    mass = float(input("Using E = mc2, enter a mass: "))
    return name, mass

# Replace spaces with ... and emoticons with emojis, then calculates energy
def process(name, mass):
    name2 = name.replace(" ", "...").replace(":)", "🙂").replace(":(", "🙁")
    c = 300000000
    massres = mass * (c * c)
    return name2, massres

# Prints entire results
def result(name2, massres):
    print()
    print(name2 )
    print(f"\"{name2}\" ")
    print(f"Characters: {len(name2)} ")
    print(f"Energy: {massres} ")

# Runs entire program
def main():
    greet()
    name, mass = insert()
    name2, massres = process(name, mass)
    result(name2, massres)

main()