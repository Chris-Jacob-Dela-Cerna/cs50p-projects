# Document: This python is my 2nd application of CS50P Week 8.

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
            raise ValueError("[Error  - System] Please enter an email.")
        if len(email) > 254:
            raise ValueError("[Error  - System] Email must not exceed 254 characters.")
        condition = r"^([a-zA-Z0-9!#$%&'*+-/=?^_`{|}~\.]+)@((?:[a-zA-Z0-9]+)(?:\.[a-zA-Z0-9]+)+)$"
        if not (email_ := re.search(condition, email)):
            raise ValueError("[Error  - System] Invalid email format.")
        username, domain = email_.groups()
        if len(username) > 64:
            raise ValueError("[Error  - System] Email username must not exceed 64 characters.")
        if len(domain) > 189:
            raise ValueError("[Error  - System] Email domain must not exceed 189 characters.")
        if username.startswith(".") or username.endswith("."):
            raise ValueError("[Error  - System] Email username must not start or end with a period.")
        if ".." in username or ".." in domain:
            raise ValueError("[Error  - System] Email username/domain must not have consecutive periods.")
        self._email = email


class Username:
    def __init__(self, username):
        self.username = username
    
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if not username:
            raise ValueError("[Error  - System] Please enter a username.")
        if len(username) > 30:
            raise ValueError("[Error  - System] Username must not exceed 30 characters.")
        condition = r"^[a-z0-9_\-\.]+$"
        if not re.search(condition, username):
            raise ValueError("[Error  - System] Invalid username format.")
        if username.startswith("_") or username.endswith("_"):
            raise ValueError("[Error  - System] Username must not start or end with an underscore.")
        if username.startswith("-") or username.endswith("-"):
            raise ValueError("[Error  - System] Username must not start or end with a hyphen.")
        if username.startswith(".") or username.endswith("."):
            raise ValueError("[Error  - System] Username must not start or end with a period.")
        if "__" in username:
            raise ValueError("[Error  - System] Username must not have consecutive underscores.")
        if "--" in username:
            raise ValueError("[Error  - System] Username must not have consecutive hyphens.")
        if ".." in username:
            raise ValueError("[Error  - System] Username must not have consecutive periods.")
        self._username = username


class Password:
    def __init__(self, password):
        self.password = password
    
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, password):
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
    username = get_username()
    get_password()


def get_email():
    print("[Prompt - System] Enter your email:")
    while True:
        try:
            email = Email(input(">>> ").strip())
        except ValueError as ve:
            print(ve)
        else:
            print("[Success - System] Email saved successfully.")
            break
    return email


def get_username():
    print("[Prompt - System] Enter your username:")
    while True:
        try:
            username = Username(input(">>> ").strip())
        except ValueError as ve:
            print(ve)
        else:
            print("[Success - System] Username saved successfully.")
            break
    return username
    

def get_password():
    ...


if __name__ == "__main__":
    main()