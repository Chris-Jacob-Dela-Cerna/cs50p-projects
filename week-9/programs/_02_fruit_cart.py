# Document: This python is my 2nd application of CS50P Week 9.

import os

abspath = os.path.abspath(__file__)
dir = os.path.dirname(abspath)
cart_path = os.path.join(dir, "02-fruit-cart")
os.makedirs(cart_path, exist_ok=True)
file_path = os.path.join(cart_path, "fruits.txt")


def main():
    print(
        "\n(<.>) I am your digital fruit cart."
        "\n      Enter your fruits 1 by 1 and I'll store them in a file."
        "\n      To finish enter 'STOP'."
    )
    cart = set()
    while True:
        fruit = input(">>> ").strip()
        if fruit == "STOP":
            break
        cart.add(fruit)

    with open(file_path, "w") as file:
        file.write("Fruits:\n")
        for item in cart:
            file.write(item + "\n")


if __name__ == "__main__":
    main()