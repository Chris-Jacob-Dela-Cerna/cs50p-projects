# Document: This python is my 1st application of CS50P Week 3.

while True:
    try:
        x, op, y = input("\nSystem:   In this format: [x op y].\n          Enter a mathematical expression.\nUser:     ").strip().split(" ")
    except ValueError:
        print("System:   Please enter a valid expression.")
    else:
        try:
            x, y = int(x), int(y)
        except ValueError:
            print("System:   Please enter a valid number.")
        else:
            break
