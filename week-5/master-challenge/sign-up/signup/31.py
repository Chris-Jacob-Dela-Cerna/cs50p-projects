# Document: This python is my last application of CS50P Week 5.

def main():
    print(
        "\n  ==================="
        "\n   Sign-up and login"
        "\n  ==================="
        "\n\nSystem:   Enter your display name to create a username."
    )
    display_name = input("User:     ")
    user_name = username(display_name)

    status = verify_username(user_name)
    if not status:
        print("System:   Invalid input.")
    

def username(display_name):
    vowels = "aeiouAEIOU"
    user_name = ""
    for character in display_name.strip():
        if character not in vowels:
            user_name += character
    return user_name


def verify_username(user_name):
    for character in user_name:
        if not character.isalnum():
            return False
    for number in range(3):
        if not user_name[number].isalpha():
            return False
    digit = 0
    for number in range(len(user_name)):
        if user_name[number].isdigit():
            digit = number
            break
    if digit != 0:
        if not user_name[digit:].isdigit():
            return False
    return True

def password():
    pass


def verify_password():
    pass


if __name__ == "__main__":
    main()