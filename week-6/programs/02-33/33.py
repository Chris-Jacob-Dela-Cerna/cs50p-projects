# Document: This python is my 2nd application of CS50P Week 6.

def main():
    print(
        "====================="
        "\n Welcome to Quizpin!"
        "\n====================="
    )
    input()
    print(
        "Select a mode:"
        "\n | a - create a quiz"
        "\n | b - start a quiz"
    )
    while True:
        user_mode = input("User:     ")
        result = check_mode(user_mode)
        match result:
            case "Create Quiz":
                if create_quiz():
                    break
            case "Start Quiz":
                if start_quiz():
                    break
            case _:
                print(f"System:   {result}")


def check_mode(user_mode):
    mode = user_mode.strip().lower()
    match mode:
        case "a":
            return "Create Quiz"
        case "b":
            return "Start Quiz"
        case _:
            return "Invalid. Please enter a valid mode."


def create_quiz():
    print("\nQuizpin:  Give me a number of items.")
    user_items = input("User:     ")
    result = check_items(user_items)
    match result:
        case "Invalid. Please enter a valid number.":
            print(f"System:   {result}")
            return False
        case _:
            print(result)
            return True


def check_items(user_items="10"):
    try:
        items = int(user_items)
    except ValueError:
        return "Invalid. Please enter a valid number."
    else:
        return items


def start_quiz():
    pass


main()