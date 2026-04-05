# Document: This python is my 1st application of CS50P Week 2.

def program():
    while True:
        response = input("\nGreetings user!\nWould you like to run calculator or match? Enter 1 or 2.\nEnter 'exit' if you want to leave.\nUser: ").strip().lower()
        if response == "exit":
            break

        elif response == "1":
            print("\nWelcome to Calculator! ")
            while True:
                calculator()
                leave = input("\nExit calculator? (yes or no)\nUser: ")
                if leave == "yes":
                    break

        elif response == "2":
            print("\nWelcome to Match! ")
            while True:
                print("BALLER")
                break

        else:
            print("Input is invalid. Please try again.")

# Implement Match









def calculator():
    while True:
        exp = input("\nEnter an expression:\nUser: ")
        x, op, y = exp.split(" ")
        x = float(x)
        y = float(y)
# Check if x and y is a number
        if op == "+" or op == "-" or op == "*" or op == "/":
            if op == "+":
                print("=", x + y)
            elif op == "-":
                print("=", x - y)
            elif op == "*":
                print("=", x * y)
            elif op == "/":
                print("=", x / y)
# Prompt user if they want to run another calculation
            break
        else:
            print("Enter a valid operator.")


program()