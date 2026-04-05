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
            print("\nWelcome to Match!", end="")
            # Placeholder
            match()
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

match_list = [
    {"name": "apple", "color": "red"},
    {"name": "banana", "color": "yellow"},
    {"name": "orange", "color": "orange"},
]

def match():
    while True:
        print("\nInstructions: You will be asked a fruit and you must match it with a color.\n")

        score = 0
        ans = input(f"Question 1: {match_list[0]["name"].title()}\nUser: ").strip().lower()
        if ans == match_list[0]["color"]:
            score += 1
        ans = input(f"Question 2: {match_list[2]["name"].title()}\nUser: ").strip().lower()
        if ans == match_list[2]["color"]:
            score += 1
        ans = input(f"Question 3: {match_list[1]["color"].title()}\nUser: ").strip().lower()
        if ans == match_list[1]["name"]:
            score += 1
        ans = input(f"Question 4: {match_list[2]["color"].title()}\nUser: ").strip().lower()
        if ans == match_list[2]["name"]:
            score += 1
        ans = input(f"Question 5: {match_list[1]["name"].title()}\nUser: ").strip().lower()
        if ans == match_list[1]["color"]:
            score += 1
        ans = input(f"Question 6: {match_list[0]["color"].title()}\nUser: ").strip().lower()
        if ans == match_list[0]["name"]:
            score += 1
        print(f"\nCongratulations! You've got a final score or {score}/6.")

        again = input("\nTry again? Enter yes or no.\nUser: ")
        if again != "yes":
            break

program()