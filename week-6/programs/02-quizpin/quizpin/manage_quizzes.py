

import os
from checker import checker
from checker import check_prefix
from checker import check_name


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
        chosen, tool = check_prefix(user, tools)
        if chosen:
            selected_quiz = checker(chosen[2:], quiz_list)
            if selected_quiz:
                break
            else:
                print("Quizpin:  Invalid. Please select a valid quiz.")
        else:
            print("Quizpin:  Invalid. Please use the right format.")

    if tool == tools["r-"]:
        rename_file(selected_quiz, quiz_path)
        input(
            "\n==============="
            "\n File renamed."
            "\n==============="
            "\n"
        )
    elif tool == tools["d-"]:
        pass


def rename_file(selected_quiz, quiz_path):
    quizzes = os.listdir(quiz_path)
    quizzes.remove(selected_quiz)
    
    print(
        f"Quizpin:  Enter the new name for '{selected_quiz}'."
    )
    while True:
        user_file = input("User:     ")
        result, file_name = check_name(user_file, quiz_path)
        match result:
            case True:
                break
            case False:
                print(f"Quizpin:  '{file_name}.csv' already exists.")
                continue
            case _:
                print("Quizpin:  Invalid. Please enter a valid file name.")
                continue

    old_quiz = os.path.join(quiz_path, selected_quiz)
    new_quiz = os.path.join(quiz_path, file_name + ".csv")
    os.rename(old_quiz, new_quiz)