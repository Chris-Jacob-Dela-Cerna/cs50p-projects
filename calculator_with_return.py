# Document: This python is my 7th application of CS50P Week 0.

def ask():
    x = float(input("What's x? "))
    op = input("What operator? ")
    y = float(input("What's y? "))
    return x, op, y

x, op, y = ask()

def solve(x, op, y):
    if op == "+":
        return round(x + y, 3)
    elif op == "-":
        return round(x - y, 3)
    elif op == "*":
        return round(x * y, 3)
    elif op == "/":
        return round(x / y, 3)
    
result = solve(x, op, y)
print(result)