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
        if result == "Create Quiz":
            if create_quiz():
                break
        elif result == "Start Quiz":
            if start_quiz():
                break
        else:
            print("System:   {result}")


def check_mode(user_mode):
    mode = user_mode.strip().lower()
    if mode == "a":
        return "Create Quiz"
    elif mode == "b":
        return "Start Quiz"
    else:
        return "Invalid. Please enter a valid mode."


def create_quiz():
    pass


def start_quiz():
    pass


main()