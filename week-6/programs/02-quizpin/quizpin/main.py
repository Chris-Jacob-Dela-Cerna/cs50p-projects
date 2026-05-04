# Document: This python is my 2nd application of CS50P Week 6.

from create_items import create_items
from start_quiz import start_quiz
from checker import checker


def main():
    input(
        "\n====================="
        "\n Welcome to Quizpin!"
        "\n====================="
        "\n"
    )

    while True:
        modes = {
            "a": "Create Quiz Items",
            "b": "Start a Quiz",
        }
        print("Quizpin:  Choose a mode:")
        for letter, mode in modes.items():
            print(f"          {letter}) {mode}")

        while True:
            user_mode = input("User:     ")
            result = checker(user_mode, modes)
            if result:
                break
            else:
                print(f"Quizpin:  Invalid. Please enter a valid mode.")

        if result == modes["a"]:
            create_items()
        elif result == modes["b"]:
            start_quiz()


if __name__ == "__main__":
    main()