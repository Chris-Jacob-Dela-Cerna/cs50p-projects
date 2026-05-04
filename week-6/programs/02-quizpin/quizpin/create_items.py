
import csv
import os


abs_filedir = os.path.abspath(__file__)
filedir = os.path.dirname(abs_filedir)
quiz_path = os.path.join(filedir, "quizzes")


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
    
    print(
        "\nQuizpin:  Name the file you'll be storing your items in."
    )
    while True:
        user_file = input("User:     ")
        result = check_name(user_file)
        if result:
            csv_path = os.path.join(quiz_path, result + ".csv")
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
    

def check_name(user_file):
    file_name = user_file.strip().replace(" ", "_")
    return file_name


def store_items(items, csv_path):
    with open(csv_path, "w", newline="") as quiz_items:
        writer = csv.DictWriter(quiz_items, fieldnames=["term", "definition"])
        writer.writeheader()
        writer.writerows(items)