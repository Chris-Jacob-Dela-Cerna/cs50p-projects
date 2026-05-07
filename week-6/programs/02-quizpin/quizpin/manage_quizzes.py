

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
        "\nL. List of Quizzes:"
        "\n"
    )

    number = 0
    quiz_list = {}
    for quiz in quizzes:
        number += 1
        quiz_list.update({str(number): quiz})
        print(f"{number}) {quiz}")
    
    input()