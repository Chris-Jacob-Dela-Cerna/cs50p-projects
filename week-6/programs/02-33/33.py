# Document: This python is my 2nd application of CS50P Week 6.

import csv


modes = ["Create Items", "Start Quiz"]
quiz_types = ["Multiple Choice", "Identification"]


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
        
        while True:
            user_mode = input("User:     ")
            result = check_mode(user_mode)
            if result in modes:
                break
            else:
                print(f"Quizpin:  {result}")

        if result == modes[0]:
            create_items()
        elif result == modes[1]:
            start_quiz()


def check_mode(user_mode):
    mode = user_mode.strip().lower()
    match mode:
        case "a":
            return modes[0]
        case "b":
            return modes[1]
        case _:
            return "Invalid. Please enter a valid mode."


def create_items():
    input(
        "\n================"
        "\n Creating quiz!"
        "\n================"
        "\n"
    )

    print(
        "Quizpin:  Give me the number of items for your quiz."
    )
    while True:
        user_items = input("User:     ")
        result = check_number(user_items)
        match result:
            case "Invalid. Please enter a valid number.":
                print(f"Quizpin:  {result}")
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
        if items < 1:
            raise ValueError
    except ValueError:
        return "Invalid. Please enter a valid number."
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
    while True:
        user_type = input("User:     ")
        result = check_type(user_type)
        if result in quiz_types:
            break
        else:
            print(f"Quizpin:  {result}")

    if result == quiz_types[0]:
        multiple_choice()
    elif result == quiz_types[1]:
        identification()


def check_type(user_type):
    type = user_type.strip().lower()
    match type:
        case "a":
            return quiz_types[0]
        case "b":
            return quiz_types[1]
        case _:
            return "Invalid. Please enter a valid quiz type."
        

def multiple_choice():
    pass


def identification():
    pass


if __name__ == "__main__":
    main()