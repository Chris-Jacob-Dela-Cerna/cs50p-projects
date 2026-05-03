# Document: This python is my 2nd application of CS50P Week 6.

import csv
import random


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
        
        modes = ["Create Items", "Start Quiz"]
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
        

def checker(user, options):
    chosen = user.strip().lower()
    match chosen:
        case "a":
            return options[0]
        case "b":
            return options[1]
        case _:
            return None


def create_items():
    input(
        "\n================"
        "\n Creating quiz!"
        "\n================"
        "\n"
    )

    print(
        "Quizpin:  Give me the number of items for your quiz."
        "\n          Minimum: 4"
    )
    while True:
        user_items = input("User:     ")
        result = check_number(user_items)
        match result:
            case None:
                print(f"Quizpin:  Invalid. Please enter a valid number.")
            case _:
                break

    print(
        "\nQuizpin:  For each item. Give me its term and definition"
        "\n          in this format: [Term - Definition]"
    )
    items = []
    for number in range(result):
        while True:
            user_item = input(f"{number + 1}) ")
            if add_item(items, user_item):
                break
            else:
                print("Quizpin:   Invalid. Please use the right format.")
    
    store_items(items)
    input(
        "\nQuizpin:  Items saved successfully."
        "\n          Select b) to start your quiz!"
        "\n"
    )


def check_number(user_items):
    try:
        items = int(user_items)
        if items < 4:
            raise ValueError
    except ValueError:
        return None
    else:
        return items


def add_item(items, user_item):
    try:
        term, definition = user_item.split(" - ")
        if term.strip() == "" or definition.strip() == "":
            raise ValueError
    except ValueError:
        return False
    else:
        items.append({"term": term, "definition": definition})
        return True


def store_items(items):
    with open("quiz_items.csv", "w", newline="") as quiz_items:
        writer = csv.DictWriter(quiz_items, fieldnames=["term", "definition"])
        writer.writeheader()
        writer.writerows(items)


def start_quiz():
    if not check_file():
        print(
            "Quizpin:  You have not created a quiz yet."
            "\n          Select a) to create a quiz!"
            "\n"
        )
        return None
    items = compile_file()

    input(
        "\n================"
        "\n Starting quiz!"
        "\n================"
        "\n"
    )

    print(
        "Quizpin:  Choose a quiz type:"
        "\n          a) Multiple Choice"
        "\n          b) Identification"
    )
    quiz_types = ["Multiple Choice", "Identification"]
    while True:
        user_type = input("User:     ")
        result = checker(user_type, quiz_types)
        if result:
            break
        else:
            print(f"Quizpin:  Invalid. Please enter a valid quiz type.")

    if result == quiz_types[0]:
        multiple_choice(items)
    elif result == quiz_types[1]:
        identification(items)
        

def check_file():
    try:
        open("quiz_items.csv")
    except FileNotFoundError:
        return False
    else:
        return True
    

def compile_file():
    items = []
    with open("quiz_items.csv") as quiz_items:
        reader = csv.DictReader(quiz_items)
        for row in reader:
            items.append({"term": row['term'], "definition": row['definition']})
    return items


def multiple_choice(quiz_items):
    quiz = convert_multiple_choice(quiz_items)
    random.shuffle(quiz)

    input(
        "\nInstructions: Read each item carefully."
        "\nChoose the letter of the correct/best answer."
        "\nWrite only the letter that corresponds to your choice"
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

    print(
        f"Congratulations! You've got a score of {score}/{idx}."
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
    pass


if __name__ == "__main__":
    main()