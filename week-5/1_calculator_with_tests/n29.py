# Document: This python is my 1st application of CS50P Week 5.

def main():
    print(
        "\nLet's do some multiplication!"
        "\nEnter two numbers [x y]."
    )
    x, y = get_numbers()
    print("Answer:", multiply(x, y))


def get_numbers():
    while True:
        try:
            x, y = input("User: ").strip().split(" ")
            x, y = int(x), int(y)
        except ValueError:
            print("Invalid numbers.")
        else:
            return x, y


def multiply(x, y):
    return x + y


if __name__ == "__main__":
    main()