

import re


class Email:
    def __init__(self, email):
        self.email = email


class Account:
    def __init__(self, username, password):
        ...


def main():
    input(
        "\n   ============"
        "\n     Sign-up"
        "\n   ============"
        "\n"
    )
    print("[Prompt - System] Enter your email:")
    email = Email(input(">>> ").strip())
    print(email.email)


if __name__ == "__main__":
    main()