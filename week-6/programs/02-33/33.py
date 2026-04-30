# Document: This python is my 2nd application of CS50P Week 6.

modes = ["Create Quiz", "Create Quiz"]


def main():
    print(
        "\n====================="
        "\n Welcome to Quizpin!"
        "\n====================="
    )

    while True:
        print(
            "\nQuizpin:  Select a mode:"
            "\n          a) create a quiz"
            "\n          b) start a quiz"
        )
        while True:

            while True:
                user_mode = input("User:     ")
                result = check_mode(user_mode)
                if result in modes:
                    break
                else:
                    print(f"System:   {result}")

            if result == modes[0]:
                if create_quiz():
                    break
            elif result == modes[1]:
                if create_quiz():
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


def create_quiz():
    print(
        "\n================"
        "\n Create a mode!"
        "\n================"
    )
    print(
        "\nQuizpin:  Give me a number of items."
    )
    while True:
        user_items = input("User:     ")
        result = check_items(user_items)
        match result:
            case "Invalid. Please enter a valid number.":
                print(f"System:   {result}")
            case _:
                print(result)
                break


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


main()