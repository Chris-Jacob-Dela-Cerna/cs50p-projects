# Document: This python is my 3rd application of CS50P Week 1.

def get_ans():
    print()
# .lower() and .strip is used to lowercase and remove whiteline from user's input before running check_color
    answer = input("Enter a color: ").lower().strip()
    return answer

def ask():
    print()
    print("Take Quiz")

    answer = get_ans()
    return answer

def check_color(answer):
    print()
# Match is used to sort whether the user's input is within the color range
    match answer:
        case "red" | "orange" | "yellow" | "green" | "blue" | "indigo" | "violet":
            print("Passed")
        case _:
            print("Failed")

def main():
    answer = ask()
    check_color(answer)

main()