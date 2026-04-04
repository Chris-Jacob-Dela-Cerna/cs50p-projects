# Document: This python is my 1st application of CS50P Week 2.

def program():
    response = input("\nCalculator or Match? (1 or 2)\nUser: ")
    if response == "1":
        print("\nWelcome to Calculator! ")
    while response == "1":
        calculator()
        leave = input("\nExit calculator? (yes or no)\nUser: ")
        if leave == "yes":
            break
    # Match


def calculator():
    while True:
        exp = input("\nEnter an expression:\nUser: ")
        x, op, y = exp.split(" ")
        x = float(x)
        y = float(y)

        if op == "+" or op == "-" or op == "*" or op == "/":
            if op == "+":
                print("=", x + y)
            elif op == "-":
                print("=", x - y)
            elif op == "*":
                print("=", x * y)
            elif op == "/":
                print("=", x / y)
            break
        else:
            print("Enter a valid operator.")


program()