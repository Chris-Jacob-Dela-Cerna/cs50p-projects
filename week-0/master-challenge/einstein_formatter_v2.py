# Document: A refactored version of Week-0's Master Challenge.

def main():
    print(
        "\n[Message -  System] Greetings user!"
    )
    user, mass = user_input()
    message, energy = process_input(user, mass)
    print_results(message, energy)


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


def process_input(user, mass):
    message = user.title().replace(" ", "...").replace(":)", "🙂").replace(":(", "🙁")
    c = 300000000
    result = mass * (c * c)
    return message, result


def print_results(message, energy):
    print(
        f"\n{message}"
        f"\n\"{message}\""
        f"\nCharacters: {len(message)}"
        f"\nEnergy: {energy}"
    )


if __name__ == "__main__":
    main()