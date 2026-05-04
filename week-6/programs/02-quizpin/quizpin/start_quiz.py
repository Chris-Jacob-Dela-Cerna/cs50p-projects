

import csv
import os
import random
from checker import checker


abs_filedir = os.path.abspath(__file__)
filedir = os.path.dirname(abs_filedir)
quiz_path = os.path.join(filedir, "quizzes")
os.makedirs(quiz_path, exist_ok=True)
quizzes = os.listdir(quiz_path)


def start_quiz():
    if not check_quizzes():
        print(
            "Quizpin:  You have not created a quiz yet."
            "\n          Select a) to create a quiz!"
            "\n"
        )
        return None
    
    print(
        "\nQuizpin:  Select a quiz to start. Type the"
        "\n          corresponding number for that quiz."
    )
    number = 0
    quiz_list = []
    for quiz in quizzes:
        number += 1
        quiz_list.append({"number": str(number), "quiz_file": quiz})
        print(f"          {number}) {quiz}")
    
    while True:
        chosen = input("User:     ")
        result = check_selected(chosen, quiz_list)
        if result:
            break
        else:
            print("Quizpin:  Invalid. Please select a valid quiz number.")
    items = decompile_file(result)

    input(
        "\n================"
        "\n Starting quiz!"
        "\n================"
        "\n"
    )

    quiz_types = {
        "a": "Multiple Choice",
        "b": "Identification",
    }
    print("Quizpin:  Choose a quiz type:")
    for letter, quiz_type in quiz_types.items():
        print(f"          {letter}) {quiz_type}")

    while True:
        chosen = input("User:     ")
        result = checker(chosen, quiz_types)
        if result:
            break
        else:
            print(f"Quizpin:  Invalid. Please enter a valid quiz type.")

    if result == quiz_types["a"]:
        multiple_choice(items)
    elif result == quiz_types["b"]:
        identification(items)
        

def check_quizzes():
    if len(quizzes) == 0:
        return False
    else:
        return True


def check_selected(chosen, quiz_list):
    for quiz in quiz_list:
        if chosen == quiz["number"]:
            return quiz["quiz_file"]
    return None
    

def decompile_file(result):
    items = []
    quiz = os.path.join(quiz_path, result)
    with open(quiz) as quiz_items:
        reader = csv.DictReader(quiz_items)
        for row in reader:
            items.append({"term": row['term'], "definition": row['definition']})
    return items


def multiple_choice(quiz_items):
    quiz = convert_multiple_choice(quiz_items)
    random.shuffle(quiz)

    input(
        "\nQuizpin:  Read each item carefully."
        "\n          Choose the letter of the correct/best answer."
        "\n          Write only the letter that corresponds to your choice."
        "\n"
    )

    score = 0
    idx = 0
    for item in quiz:
        idx += 1
        print(f"{idx}) {item['question']}")
        for letter, choice in item["choices"].items():
            print(f"{letter}. {choice}")
        user_answer = input("User:     ").strip().lower()
        try:
            if item["choices"][user_answer] == item["answer"]:
                score += 1
        except KeyError:
            pass

    input(
        "\n=================="
        "\n Congratulations!"
        f"\n You got {score}/{idx}."
        "\n=================="
        "\n"
    )


def convert_multiple_choice(quiz_items):
    quiz = []
    all_terms = [item["term"] for item in quiz_items if item["term"]]
    for item in quiz_items:
        question = item["definition"]
        answer = item["term"]
        problem = {"question": question, "answer": answer, "choices": {}}

        terms = [term for term in all_terms if term != answer]

        choices = [answer]
        choices.extend(random.sample(terms, 3))
        random.shuffle(choices)

        letters = "abcd"
        problem["choices"].update(zip(letters, choices))
        quiz.append(problem)
    return quiz


def identification(quiz_items):
    quiz = convert_identification(quiz_items)
    random.shuffle(quiz)

    input(
        "\nQuizpin:  Read each statement carefully."
        "\n          Identify the term or concept being described "
        "\n          and write your answer in the space provided."
        "\n"
    )

    score = 0
    idx = 0
    for item in quiz:
        idx += 1
        print(f"{idx}) {item['question']}")
        user_answer = input("User:     ").strip().lower()
        if user_answer == item["answer"].strip().lower():
            score += 1

    input(
        "\n=================="
        "\n Congratulations!"
        f"\n You got {score}/{idx}."
        "\n=================="
        "\n"
    )


def convert_identification(quiz_items):
    quiz = []
    for item in quiz_items:
        question = item["definition"]
        answer = item["term"]
        problem = {"question": question, "answer": answer}
        quiz.append(problem)
    return quiz