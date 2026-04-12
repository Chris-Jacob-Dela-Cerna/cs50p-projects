# Document: This python is my 1st application of CS50P Week 3.

stroperators = ["+", "-", "*", "/"]

while True:
    try:
        x, op, y = input("\nSystem:   In this format: [x op y].\n          Enter a mathematical expression.\nUser:     ").strip().split(" ")
    except ValueError:
        print("System:   Please enter a valid expression.")
        continue
    else:
        try:
            x, y = int(x), int(y)
        except ValueError:
            print("System:   Please enter a valid number.")
            continue
        else:
            if not op in stroperators:
                print("System:   Please enter a valid operator.")
                continue
            else:
                if op == "+":
                    expression = x + y
                elif op == "-":
                    expression = x - y
                elif op == "*":
                    expression = x * y
                else:
                    expression = x / y
                break
print(f"System:   The answer is {expression}.")