# Document: This python is my 1st application of CS50P Week 5.

def main():
    print(
        "\nLet's do some calculation!"
        "\nEnter two numbers [x op y]."
    )
    x, op, y = get_numbers()
    match op:
        case "+":
            answer = addition(x, y)
        case "-":
            answer = subtraction(x, y)
        case "*":
            answer = multiply(x, y)
        case "/":
            answer = divide(x, y)
    print("Answer:", answer)

operators = ["+", "-", "*", "/"]

def get_numbers():
    while True:
        try:
            x, op, y = input("User: ").strip().split(" ")
            x, y = int(x), int(y)
            if op not in operators:
                raise ValueError
        except ValueError:
            print("Invalid expression.")
        else:
            return x, op, y


def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


if __name__ == "__main__":
    main()