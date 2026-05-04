# Document: This python is my 2nd application of CS50P Week 6.

import os
from create_items import create_items
from start_quiz import start_quiz


abs_filedir = os.path.abspath(__file__)
filedir = os.path.dirname(abs_filedir)
quiz_path = os.path.join(filedir, "quizzes")
os.makedirs(quiz_path, exist_ok=True)
quizzes = os.listdir(quiz_path)


def main():
    input(
        "\n====================="
        "\n Welcome to Quizpin!"
        "\n====================="
        "\n"
    )

    while True:
        print(
            "Quizpin:  Choose a mode:"
            "\n          a) Create Quiz Items"
            "\n          b) Start a Quiz"
        )
        
        modes = {
            "a": "Create Items",
            "b": "Start Quiz",
        }
        while True:
            user_mode = input("User:     ")
            result = checker(user_mode, modes)
            if result:
                break
            else:
                print(f"Quizpin:  Invalid. Please enter a valid mode.")

        if result == modes[0]:
            create_items()
        elif result == modes[1]:
            start_quiz()


def checker(user, modes):
    chosen = user.strip().lower()
    match chosen:
        case "a":
            return modes[0]
        case "b":
            return modes[1]
        case _:
            return None
        

if __name__ == "__main__":
    main()