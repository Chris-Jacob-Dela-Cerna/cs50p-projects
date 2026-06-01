# Document: This python is my 3rd application of CS50P Week 0.

# Greets user and asks what operation will be used.
print( )
print("Hello user! I am your simple 2-constant calculator. ")
op = input("To start, what operation will be executed? \nChoose from: + , - , * , / : ").strip()

# Asks for the 2 constants provided by the user
print( )
print("Great! Now we'll need 2 variables. ")
x = int(input("What's the first constant? (The number on the left): "))
y = int(input("Nice! How about the second constant? (The number on the right): "))

# Asks the user for clarification
print( )
print(f"Okay, just to clarify. Your expression is {x} {op} {y}. ")
out = input("Is this correct? \nType yes or no: ").strip().lower()

print( )
# Check if user said yes or no
if out == "yes":    
    if op == "+":
        print("The answer is:",x + y)
    elif op == "-":
        print("The answer is:",x - y)
    elif op == "*":
        print("The answer is:",x * y)
    elif op == "/":
        print("The answer is:",x / y)
    else:
        print("Invalid operation. ")
elif out == "no":
    print("Ohh okayyy... you'll have to restart the python since idk how to reset a program yet :( ")

print( )