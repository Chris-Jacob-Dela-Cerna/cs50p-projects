# Document: This python is my 8th application of CS50P Week 0.

# Prompts user's name
def greet():
    name = input("Hello user, what's your name? ").strip().title()
    return name

# Prompts user for a few values
def ask():
    x = float(input("What's x? "))
    op = input("What operator? ")
    y = float(input("What's y? "))
    return x, op, y

# Checks operator, then solves
def solve(x, op, y):
    if op == "+":
        return round(x + y, 3)
    elif op == "-":
        return round(x - y, 3)
    elif op == "*":
        return round(x * y, 3)
    elif op == "/":
        return round(x / y, 3)

# Runs entire program
def main():
    name = greet()
    print(f"Greetings {name}! ")
    x, op, y = ask()
    result = solve(x, op, y)
    print(f"The answer is {result}. ")

main()