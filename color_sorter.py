# Document: This python is my 3rd application of CS50P Week 1.

def get_ans():
    print()
    answer = input("Enter a color: ").lower().strip()
    return answer

def ask():
    print()
    print("Take Quiz")

    answer = get_ans()
    return answer

def check_color(answer):
    print()
    match answer:
        case "red" | "orange" | "yellow" | "green" | "blue" | "indigo" | "violet":
            print("Passed")
        case _:
            print("Failed")

def main():
    answer = ask()
    check_color(answer)

main()