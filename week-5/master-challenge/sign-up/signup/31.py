# Document: This python is my last application of CS50P Week 5.

def main():
    print(
        "\n  ==================="
        "\n   Sign-up and login"
        "\n  ==================="
        "\n\nSystem:   Enter your display name to create a username."
    )
    while True:
        display_name = input("User:     ")
        user_name = username(display_name)
        status, message = verify_username(user_name)
        input(f"System:   {message} ")
        if status:
            break
    print(
        "\n  ====================="
        "\n   Setup your password"
        "\n  ====================="
        "\n\nSystem:   Enter your desired password."
    )


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
            return False, "Invalid. There must only be letters and numbers."
    for number in range(3):
        if not user_name[number].isalpha():
            return False, "Invalid. The first 3 characters should be letters."
    digit = 0
    for number in range(len(user_name)):
        if user_name[number].isdigit():
            digit += number
            break
    if digit != 0:
        if not user_name[digit:].isdigit():
            return False, "Invalid. After the 1st number, the rest should be numbers."
        
    code = ""
    for character in user_name:
        if code == "":
            if character == "5":
                code += "5"
        elif code == "5":
            if character == "2":
                code += "2"

    if code == "52":
        return True, f"Admin [{user_name}] saved successfully."
    else:
        return True, f"Username [{user_name}] saved successfully."


def password():
    pass


def verify_password():
    pass


if __name__ == "__main__":
    main()