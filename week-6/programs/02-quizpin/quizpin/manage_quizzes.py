

import os
from checker import checker


def manage_quizzes():
    abs_filedir = os.path.abspath(__file__)
    filedir = os.path.dirname(abs_filedir)
    quiz_path = os.path.join(filedir, "quizzes")
    os.makedirs(quiz_path, exist_ok=True)
    quizzes = os.listdir(quiz_path)

    print(
        "\nQuizpin:  Type r-[number] to rename the quiz."
        "\n          Type d-[number] to delete the quiz."
        "\n          Example: r-2"
    )

    number = 0
    quiz_list = {}
    print("\nList of Quizzes:")
    for quiz in quizzes:
        number += 1
        quiz_name = quiz[:-4].replace("_", " ")
        quiz_list.update({str(number): quiz})
        print(f"{number}) {quiz_name}")

    tools = {
        "r-": "rename",
        "d-": "delete",
    }
    while True:
        user = input("\nUser:     ")
        result = check_manage(user, tools)
        if result:
            break

    if result == tools["r-"]:
        pass
    elif result == tools["d-"]:
        pass


def check_manage(user, tools):
    chosen = user.strip().lower()
    for key, tool in tools.items():
        if chosen.startswith(key):
            return tool
    else:
        return None