# Document: A refactored version of Week-0's Master Challenge.

def main():
    print(
        "\n[Message -  System] Greetings user!"
    )
    message, mass = user_input()
    converted, result = process_input(message, mass)


def user_input():
    print("[Prompt  -  System] Please enter a message.")
    message = input("[User    -  System] ").strip()

    print("[Prompt  -  System] Using E = mc^2, enter a mass.")
    while True:
        user = input("[User    -  System] ").strip()
        try:
            mass = float(user)
        except ValueError:
            print("[Error   -  System] Invalid number.")
        else:
            break
    return message, mass


def process_input(message, mass):
    converted = message.title().replace(" ", "...").replace(":)", "🙂").replace(":(", "🙁")
    c = 300000000
    result = mass * (c * c)
    return converted, result


if __name__ == "__main__":
    main()