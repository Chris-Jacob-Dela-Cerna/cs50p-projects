# Document: This python is my last application of CS50P Week 5.

def main():
    while True:
        user_password = input("User:     ").strip()
        status, data = check_password(user_password)
        if status:
            status, data = verify_password(data)
            if status:
                break
        print(f"System:   {data}")



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
        status, data = verify_username(username)
        print(f"System:   {data} ")
        if status:
            status, data = check_admin(username)
            if status:
                print(f"System:   {data}")
            break
    input()
    print(
        "  ====================="
        "\n   Setup your password"
        "\n  ====================="
        "\n\nSystem:   Enter your desired password."
    )
    # Temporarily move password for testing



def convert_username(display_name):
    vowels = "aeiouAEIOU"
    username = ""
    for character in display_name:
        if character not in vowels:
            username += character
    return username


def verify_username(user_name):
    if len(user_name) < 3:
        return False, "Invalid. There must be 3 or more characters."
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
    characters = len(user_password)
    if characters < 9:
        return False, "Invalid. There must be 9 or more characters."
    if " " in user_password:
        return False, "Invalid. There must be no spaces."
    
    letters = 0
    uppercase = 0
    lowercase = 0
    numbers = 0
    symbols = 0
    for character in user_password:
        if character.isalpha():
            letters += 1
            if character.isupper():
                uppercase += 1
            elif character.islower():
                lowercase += 1
        elif character.isdigit():
            numbers += 1
        else:
            symbols += 1
    
    character_data = {}
    character_data.update(
        {
        "characters": characters,
        "letters": letters,
        "uppercase": uppercase,
        "lowercase": lowercase,
        "numbers": numbers,
        "symbols": symbols,
        }
    )
    return True, character_data


def verify_password(data):
    percentage = {
        "uppercase": round((data["uppercase"]/data["characters"]) * 100, 2),
        "lowercase": round((data["lowercase"]/data["characters"]) * 100, 2),
        "numbers": round((data["numbers"]/data["characters"]) * 100, 2),
        "symbols": round((data["symbols"]/data["characters"]) * 100, 2),
    }
    print(percentage)

    score = 0
    for key in percentage.keys():
        if 26 >= percentage[key] >= 24:
            score += 10
        elif 35 >= percentage[key] >= 15:
            score += 9
        elif 40 >= percentage[key] >= 10:
            score += 7
        else:
            score += 4
    print(score)

    return True, None
    

if __name__ == "__main__":
    main()