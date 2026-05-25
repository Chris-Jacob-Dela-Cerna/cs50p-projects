

import sys


class Fruits:
    def __init__(self, name, color):
        if not name or not color:
            raise ValueError
        self.name = name
        self.color = color


def main():
    fruit = get_fruits()
    print(f"[Succeed - System] {fruit.name} is {fruit.color}.")


def get_fruits():
    name = input("[Prompt - System] Fruit: ").strip()
    color = input("[Prompt - System] Color: ").strip()
    try:
        return Fruits(name, color)
    except ValueError:
        sys.exit("[Error  - System] Invalid input.")



if __name__ == "__main__":
    main()