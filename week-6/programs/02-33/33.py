# Document: This python is my 2nd application of CS50P Week 6.


def main():
    print(
        "====================="
        "\n Welcome to Quizpin!"
        "\n====================="
    )
    input()
    print(
        "Quizpin:"
        "\n | a - create a quiz"
        "\n | b - start a quiz"
    )
    while True:
        user_mode = input("User:   ")
        mode = check_mode(user_mode)
        if mode == "Create Quiz":
            create_quiz()
            break
        elif mode == "Start Quiz":
            start_quiz()
            break


def check_mode(user_mode):
    mode = user_mode.strip().lower()
    if mode == "a":
        return "Create Quiz"
    elif mode == "b":
        return "Start Quiz"
    else:
        return False


def create_quiz():
    pass


def start_quiz():
    pass


main()