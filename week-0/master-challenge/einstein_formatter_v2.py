# Document: A refactored version of Week-0's Master Challenge.

def main():
    print(
        "\n[Message -  System] Greetings user!"
    )
    name = user_input()


def user_input():
    print("[Prompt  -  System] Please enter your name.")
    name = input("[User    -  System] ").strip()
    return name


if __name__ == "__main__":
    main()