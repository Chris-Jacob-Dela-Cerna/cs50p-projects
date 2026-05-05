

import csv
import os


def create_items():
    input(
        "\n================"
        "\n Creating quiz!"
        "\n================"
        "\n"
    )

    print(
        "Quizpin:  Give me the number of items for your quiz."
        "\n          Note: Minimum of 4 items."
    )
    while True:
        user_items = input("User:     ")
        result = check_number(user_items)
        if result:
            break
        else:
            print(f"Quizpin:  Invalid. Please enter a valid number.")
                
    print(
        "\nQuizpin:  For each item. Give me its term and definition"
        "\n          in this format: [Term - Definition]"
        "\n          Note: You cannot repeat a term."
    )
    items = []
    for number in range(result):
        while True:
            user_item = input(f"{number + 1}) ")
            if add_item(user_item, items):
                break
            else:
                print("Quizpin:  Invalid. Please use the right format.")
    
    abs_filedir = os.path.abspath(__file__)
    filedir = os.path.dirname(abs_filedir)
    quiz_path = os.path.join(filedir, "quizzes")
    os.makedirs(quiz_path, exist_ok=True)
    print(
        "\nQuizpin:  Name the file you'll be storing your items in."
    )
    while True:
        user_file = input("User:     ")
        result, file_name = check_name(user_file, quiz_path)
        match result:
            case True:
                break
            case False:
                print(
                    f"Quizpin:  '{file_name}.csv' already exists."
                    "\n          Would you like to overwrite? Enter y or n."
                )
                user_select = input("User:     ")
                if not overwrite(user_select):
                    print("Quizpin:  Name the file you'll be storing your items in.")
                    continue
            case _:
                print("Quizpin:  Invalid. Please enter a valid file name.")
                continue
        csv_path = os.path.join(quiz_path, file_name + ".csv")
        break

    store_items(items, csv_path)
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


def add_item(user_item, items):
    try:
        term, definition = user_item.split(" - ")
        term = term.strip()
        definition = definition.strip()
        if term == "" or definition == "":
            raise ValueError
        for item in items:
            if term.lower() == item["term"].lower():
                raise ValueError
    except ValueError:
        return False
    else:
        items.append({"term": term, "definition": definition})
        return True
    

def check_name(user_file, quiz_path):
    file_name = user_file.strip().replace(" ", "_")
    for quiz in os.listdir(quiz_path):
        if file_name == quiz[:-4]:
            return False, file_name
        elif file_name == "":
            return None, None
    return True, file_name


def overwrite(user_select):
    chosen = user_select.strip().lower()
    if chosen == "y":
        return True
    return False

def store_items(items, csv_path):
    with open(csv_path, "w", newline="") as quiz_items:
        writer = csv.DictWriter(quiz_items, fieldnames=["term", "definition"])
        writer.writeheader()
        writer.writerows(items)