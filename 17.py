# Document: This python is my 1st application of CS50P Week 2.

def program():
    print("\nGreetings user!", end="")
    while True:
        response = input("\nWould you like to run calculator or match? Enter 1 or 2.\nEnter 'exit' to end the program.\nUser: ").strip().lower()
        if response == "exit":
            break

        elif response == "1":
            print("\nWelcome to Calculator!", end="")
            calculator()
            print("Thank you for using Calculator.")

        elif response == "2":
            print("\nWelcome to Match!")
            # Placeholder
            print("BALLER")
            print("Thank you for using Match.")

        else:
            print("Input is invalid. Please try again.\n")



def calculator():
    while True:
        exp = input("\nEnter an expression:\nUser: ")
        x, op, y = exp.split(" ")
        x = float(x)
        y = float(y)
# Check if x and y is a number

        if op == "+" or op == "-" or op == "*" or op == "/":
            match op:
                case "+":
                    print("=", x + y)
                case "-":
                    print("=", x - y)
                case "*":
                    print("=", x * y)
                case "/":
                    print("=", x / y)
            if_calcu = input("\nWant to do another calculation? Enter yes or no.\nUser: ").strip().lower()
            if if_calcu != "yes":
                break

        else:
            print("Enter a valid operator.")


# Implement match()
def match():
    print("BALLER")

program()