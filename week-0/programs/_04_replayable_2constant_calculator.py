# Document: This python is my 4th application of CS50P Week 0.

# Defines greet()
def greet(to="user."):
# Greets user
    print()
    print("Greetings", to)
    print()

# Defines main()
def main():
# Asks the user for constants
    x = float(input("Enter x: "))
    op = input("Enter operation \n( + , - , * , / ): ")
    y = float(input("Enter y: "))
# Iterates the full expression
    print(x, op, y, "= ", end="")
# Executes solve()    
    solve(x, op, y)
    
# Defines solve()
def solve(x, op, y):
# Checks the operator used
    if op == "+":
        print(round(x + y, 5))
    elif op == "-":
        print(round(x - y, 5))
    elif op == "*":
        print(round(x * y, 5))
    elif op == "/":
        print(round(x / y, 5))
    else:
        print("Invalid operation.")
    again()

# Defines again()
def again():
# Asks user if they will continue
    out = input("Try again? \n(Type y or n): ").strip().lower()
    print()
# Checks the user's response
    if out == "y":
        main()
    elif out == "n":
        exit

# Greets user and runs main()
greet()
main()