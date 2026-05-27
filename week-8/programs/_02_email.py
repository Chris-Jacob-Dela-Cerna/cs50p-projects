

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
        if len(email) > 254:
            raise ValueError(2)
        condition = r"^([a-zA-Z0-9!#$%&'*+-/=?^_`{|}~]+)@((?:[a-zA-Z0-9]+)(?:\.[a-zA-Z0-9]+)+)$"
        if not (email_ := re.search(condition, email)):
            raise ValueError(3)
        username, domain = email_.groups()
        if len(username) > 64:
            raise ValueError(4)
        if len(domain) > 189:
            raise ValueError(5)
        if username.startswith(".") or username.endswith("."):
            raise ValueError(6)
        if ".." in username or ".." in domain:
            raise ValueError(7)
        self._email = email


class Username:
    def __init__(self, username):
        self.username = username
    
    @property
    def email(self):
        return self._username
    
    @email.setter
    def email(self, username):
        self._username = username


class Password:
    def __init__(self, password):
        self.password = password
    
    @property
    def email(self):
        return self._password
    
    @email.setter
    def email(self, password):
        self._password = password


def main():
    print(
        "\n ===================="
        "\n  Sign-up with Email"
        "\n ===================="
        "\n"
    )
    email = get_email()
    
    print(
        "\n ======================="
        "\n  Username and Password"
        "\n ======================="
        "\n"
    )
    get_username()
    get_password()

    


def get_email():
    print("[Prompt - System] Enter your email:")
    while True:
        try:
            email = Email(input(">>> ").strip())
        except ValueError as ve:
            if ve.args[0] == 1:
                print("[Error  - System] Please enter an email.")
            elif ve.args[0] == 2:
                print("[Error  - System] Email must not exceed 254 characters.")
            elif ve.args[0] == 3:
                print("[Error  - System] Invalid email format.")
            elif ve.args[0] == 4:
                print("[Error  - System] Email username must not exceed 64 characters.")
            elif ve.args[0] == 5:
                print("[Error  - System] Email domain must not exceed 189 characters.")
            elif ve.args[0] == 6:
                print("[Error  - System] Email username must not start or end with a period.")
            elif ve.args[0] == 7:
                print("[Error  - System] Email username/domain must not have consecutive periods.")
        else:
            print("[Success - System] Email saved successfully.")
            break
    return email


def get_username():
    print("[Prompt - System] Enter your username:")
    

def get_password():
    ...


if __name__ == "__main__":
    main()