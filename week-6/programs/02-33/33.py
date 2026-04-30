# Document: This python is my 2nd application of CS50P Week 6.

modes = ["Create Items", "Start Quiz"]


def main():
    print(
        "\n====================="
        "\n Welcome to Quizpin!"
        "\n====================="
    )

    while True:
        print(
            "\nQuizpin:  Select a mode."
            "\n          a) create quiz items"
            "\n          b) start a quiz"
        )
        
        while True:
            user_mode = input("User:     ")
            result = check_mode(user_mode)
            if result in modes:
                break
            else:
                print(f"Quizpin:  {result}")

        if result == modes[0]:
            if create_items():
                break
        elif result == modes[1]:
            if start_quiz():
                break


def check_mode(user_mode):
    mode = user_mode.strip().lower()
    match mode:
        case "a":
            return modes[0]
        case "b":
            return modes[1]
        case _:
            return "Invalid. Please enter a valid mode."


def create_items():
    print(
        "\n================"
        "\n Create a quiz!"
        "\n================"
        "\n"
        "\nQuizpin:  Give me the number of items."
    )

    while True:
        user_items = input("User:     ")
        result = check_number(user_items)
        match result:
            case "Invalid. Please enter a valid number.":
                print(f"Quizpin:  {result}")
            case _:
                break

    print(
        "\nQuizpin:  For each of the items."
        "\n          Give me its term and definition in this format:"
        "\n          [Term - Definition]"
    )

    items = []
    for number in range(result):
        while True:
            user_item = input(f"{number + 1}) ")
            if add_item(items, user_item):
                break
            else:
                print("Quizpin:   Invalid. Please use the right format.")
    store_items(items)


def check_number(user_items):
    try:
        items = int(user_items)
        if items < 1:
            raise ValueError
    except ValueError:
        return "Invalid. Please enter a valid number."
    else:
        return items


def add_item(items, user_item):
    try:
        term, definition = user_item.split(" - ")
        if term.strip() == "" or definition.strip() == "":
            raise ValueError
    except ValueError:
        return False
    else:
        item = f"{term},{definition}"
        items.append(item)
        return True


def store_items(items):
    with open("items.csv", "w") as quiz_items:
        for item in items:
            quiz_items.write(f"{item}\n")


def start_quiz():
    pass


if __name__ == "__main__":
    main()