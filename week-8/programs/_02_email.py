

import re


class Email:
    def __init__(self, email):
        self.email = email
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email):
        if not email:
            raise ValueError(1)
        condition = r"^([a-zA-Z0-9!#$%&'*+-/=?^_`{|}~]+)@([a-zA-Z0-9]+)(\.[a-zA-Z0-9]+)+$"
        if not re.search(condition, email):
            raise ValueError(2)
        self._email = email


class Account:
    def __init__(self, username, password):
        ...


def main():
    input(
        "\n ===================="
        "\n  Sign-up with Email"
        "\n ===================="
        "\n"
    )
    print("[Prompt - System] Enter your email:")
    while True:
        try:
            email = Email(input(">>> ").strip())
        except ValueError as ve:
            if ve.args[0] == 1:
                print("[Error  - System] Please enter an email.")
            elif ve.args[0] == 2:
                print("[Error  - System] Invalid email format.")
        else:
            print("[Success - System] Email saved successfully.")
            break


if __name__ == "__main__":
    main()