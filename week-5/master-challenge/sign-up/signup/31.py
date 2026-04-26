# Document: This python is my last application of CS50P Week 5.

def main():
    input()
    print(
        "  ==================="
        "\n   Sign-up and login"
        "\n  ==================="
        "\n\nSystem:   Enter your display name to create a username."
    )
    while True:
        display_name = input("User:     ").strip()
        username = convert_username(display_name)
        status, message = verify_username(username)
        print(f"System:   {message} ")
        if status:
            status, message = check_admin(username)
            if status:
                print(f"System:   {message}")
            break
    input()
    print(
        "  ====================="
        "\n   Setup your password"
        "\n  ====================="
        "\n\nSystem:   Enter your desired password."
    )
    user_password = input("User:     ").strip()
    password = check_password(user_password)


def convert_username(display_name):
    vowels = "aeiouAEIOU"
    username = ""
    for character in display_name:
        if character not in vowels:
            username += character
    return username


def verify_username(user_name):
    if not user_name.isalnum():
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
        
    return True, f"Username [{user_name}] saved successfully."
        

def check_admin(user_name):
    code = ""
    for character in user_name:
        if code == "":
            if character == "5":
                code += "5"
        elif code == "5":
            if character == "2":
                code += "2"

    if code == "52":
        return True, f"Admin permissions granted."
    else:
        return False, None
        

def check_password(user_password):
    for character in user_password:
        if character == " ":
            return False, "Invalid. There must be no spaces."



def verify_password():
    pass


if __name__ == "__main__":
    main()