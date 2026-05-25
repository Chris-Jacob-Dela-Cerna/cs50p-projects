

import sys


class Fruits:
    def __init__(self, name, color):
        if not name or not color:
            raise ValueError
        self.name = name
        self.color = color

    def __str__(self):
        return f"I'mma {self.name} n I'mma {self.color}."
    
    def angry(self):
        return self.name.upper()


def main():
    fruit = get_fruits()
    print(f"[Succeed - System] {fruit.name} is {fruit.color}.")
    fruit2 = get_fruits()
    print(f"[Succeed - System] {fruit2.name} is {fruit2.color} unlike {fruit.name}.")
    input()
    print(fruit)
    print(fruit2.angry())


def get_fruits():
    name = input("[Prompt - System] Fruit: ").strip()
    color = input("[Prompt - System] Color: ").strip()
    try:
        return Fruits(name, color)
    except ValueError:
        sys.exit("[Error  - System] Invalid input.")



if __name__ == "__main__":
    main()