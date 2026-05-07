

import os
from checker import checker


def manage_quizzes():
    abs_filedir = os.path.abspath(__file__)
    filedir = os.path.dirname(abs_filedir)
    quiz_path = os.path.join(filedir, "quizzes")
    os.makedirs(quiz_path, exist_ok=True)
    quizzes = os.listdir(quiz_path)

    input(
        "\nQuizpin:  Type r-[number] to rename the quiz."
        "\n          Type d-[number] to delete the quiz."
        "\n          Example: r-2"
        "\n"
    )

    number = 0
    quiz_list = {}
    print("List of Quizzes:")
    for quiz in quizzes:
        number += 1
        quiz_name = quiz[:-4].replace("_", " ")
        quiz_list.update({str(number): quiz})
        print(f"{number}) {quiz_name}")
    print()

    tools = {
        "r-": "rename",
        "d-": "delete",
    }
    while True:
        user = input("User:     ")
        chosen, tool = check_manage(user, tools)
        if chosen:
            result = checker(chosen[2:], quiz_list)
            if result:
                break
            else:
                print("Quizpin:  Invalid. Please select a valid quiz.")
        else:
            print("Quizpin:  Invalid. Please use the right format.")

    if tool == tools["r-"]:
        pass
    elif tool == tools["d-"]:
        pass


def check_manage(user, tools):
    chosen = user.strip().lower()
    for key, tool in tools.items():
        if chosen.startswith(key):
            return chosen, tool
    else:
        return None, None, None