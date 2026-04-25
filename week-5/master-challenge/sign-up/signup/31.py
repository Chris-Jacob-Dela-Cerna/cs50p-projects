# Document: This python is my last application of CS50P Week 5.

def main():
    print(
        "\n  ==================="
        "\n   Sign-up and login"
        "\n  ==================="
        "\n\nSystem:   Enter your display name to create a username."
    )
    display_name = input("User:     ")
    name = username(display_name)
    print(name)
    

def username(display_name):
    vowels = "aeiouAEIOU"
    name = ""
    for character in display_name.strip():
        if character not in vowels:
            name += character
    return name


def verify_username():
    pass


def password():
    pass


def verify_password():
    pass


if __name__ == "__main__":
    main()