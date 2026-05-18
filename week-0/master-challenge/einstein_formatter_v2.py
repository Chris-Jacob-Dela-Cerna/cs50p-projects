# Document: A refactored version of Week-0's Master Challenge.

def main():
    print(
        "\n[Message -  System] Greetings user!"
    )
    name = user_input()


def user_input():
    print("[Prompt  -  System] Please enter your name.")
    name = input("[User    -  System] ").strip()

    print("[Prompt  -  System] Using E = mc^2, enter a mass.")
    while True:
        user = input("[User    -  System] ").strip()
        try:
            mass = float(user)
        except ValueError:
            print("[Error   -  System] Invalid number.")
        else:
            break
    return name, mass


if __name__ == "__main__":
    main()