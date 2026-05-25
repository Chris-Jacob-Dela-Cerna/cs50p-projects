

class Fruits:
    ...


def main():
    fruit = get_fruits()
    print(fruit.name, fruit.color)


def get_fruits():
    name = input("Enter fruit: ").strip()
    color = input("Enter color: ").strip()
    return Fruits(name, color)



if __name__ == "__main__":
    main()