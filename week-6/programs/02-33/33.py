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


items = []


def create_items():
    print(
        "\n================"
        "\n Create a mode!"
        "\n================"
        "\n"
        "\nQuizpin:  Give me a number of items."
    )

    while True:
        user_items = input("User:     ")
        result = check_items(user_items)
        match result:
            case "Invalid. Please enter a valid number.":
                print(f"Quizpin:  {result}")
            case _:
                break

    print(
        f"\nQuizpin:  For each of the {result} items."
        "\n          Give me the term and definition in this format:"
        "\n          >>> Term - Definition"
    )

    while True:
        for number in range(result):
            user_item = input(f"\n{number + 1}) ")
        if add_items(user_item):
            break


def add_items(user_item):
    term, definition = user_item.split(" - ")
    item = f"{term},{definition}"
    items.append(item)

    with open("items.csv", "w") as quiz_items:
        for item in items:
            quiz_items.write(f"{item}\n")
    return True


def check_items(user_items):
    try:
        items = int(user_items)
        if items < 1:
            raise ValueError
    except ValueError:
        return "Invalid. Please enter a valid number."
    else:
        return items


def start_quiz():
    pass


if __name__ == "__main__":
    main()