# Document: This python is my last application of CS50P Week 4.

import sys
import requests
import pyfiglet
import random
import emoji
import inflect

# The coincap api_key is hidden to protect my data when pushing to github
api_key = ""
figlet_fonts = pyfiglet.FigletFont.getFonts()
pyinflect = inflect.engine()


def main():
    arg_result = check_args()
    if arg_result == 0:
        airport()
    elif arg_result == 1:
        bitcoin_api = check_net()
        if not bitcoin_api:
            sys.exit()
        destination(bitcoin_api)
    else:
        sys.exit()
        
        
def check_args():
    try:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            return 0
        else:
            if float(sys.argv[1]) < 0:
                raise ValueError
            return 1
    except IndexError, ValueError:
        print(
            "System:   Invalid command-line argument."
            f"\n          >>> python {sys.argv[0]} [input]"
        )


def airport():
    user_font = check_font()
    if not user_font:
        print(
            "System:   Invalid font."
            f"\n          >>> python {sys.argv[0]} {sys.argv[1]} [input]"
        )
        sys.exit()
    identity_banner(user_font)
    review()
    flight_delay()


def check_font():
    if len(sys.argv) < 3:
        return random.choice(figlet_fonts)
    elif sys.argv[2] in figlet_fonts:
        return sys.argv[2]
    else:
        return None

        
def identity_banner(user_font):
    print(
        "\n< With a flight heading to the Philippines, your group arrives at the airport >"
        "\n< While waiting for your plane, you spot a font dashboard >"
        "\n< The dashboard lets you enter text and convert it into the font you selected >"
    )
    user_text = input("\nUser:     ").strip()
    header = pyfiglet.figlet_format("Welcome Traveller!", font="mini")
    message = pyfiglet.figlet_format(user_text, font=user_font)
    print(header, end="")
    print(message, end="")


def review():
    print(
        "\n< A service personnel approached you and asked how was your experience at the airport >"
        "\n< Express your thoughts with the help of emojis >"
    )
    user_text = input("\nUser:     ").strip()
    message = emoji.emojize(user_text)
    print("Review:   " + message)


def flight_delay():
    print(
        "\n< The service crew called out everyone with a flight to the Philippines >"
        "\n< You are informed that the flight is currently delayed >"
        "\n< To pass the time, your group decides to play a game >"
    )
    adieu()
    print(
        "\n< The plane will arrive in 30 minutes >"
        "\n< Your friend opened their pocket console and started a game >"
        "\n< He wants you to play a number guessing game >"
    )
    guessing_game()


def adieu():
    print(
        "\nSystem:   Enter the names of your travel buddies 1 by 1."
        "\n          Enter 'ctrl-z' to finish."
    )
    names = []
    while True:
        try:
            name = input("User:     ").strip()
        except EOFError:
            if len(names) != 0:
                names.sort()
                break
            print("System:   Invalid amount of names.")
        else:
            if name != "":
                names.append(name.title())
    message = pyinflect.join(names)
    print(f"System:   Adieu, adieu, to {message}.")


def guessing_game():
    max_level = 100
    user_level = get_level(max_level)
    random.seed(user_level)

    max_integers = random.randint(2, 1000)
    correct = random.randint(1, max_integers)
    print(
        f"\nSystem:   Level {user_level}:"
        f"\n          Guess the number from 1-{max_integers}."
    )
    
    while True:
        try:
            user_number = int(input("User:     ").strip())
            if not 0 < user_number <= max_integers:
                raise ValueError
        except ValueError:
            print("System:   Invalid number.")
        else:
            if user_number > correct:
                print("System:   Too large!")
            elif user_number < correct:
                print("System:   Too small!")
            else:
                print(f"System:   Correct! Congratulations for guessing the number {correct}.")
                break


def get_level(max_level):
    print(f"\nSystem:   Enter a level from 1-{max_level}.")
    while True:
        try:
            user_level = int(input("User:     ").strip())
            if not 0 < user_level <= max_level:
                raise ValueError
        except ValueError:
            print("System:   Invalid number.")
        else:
            break
    return user_level


def check_net():
    try:
        bitcoin_api = requests.get(
            f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={api_key}"
            )
    except requests.RequestException:
        print("System:   [Connection timeout]")
        return None
    else:
        bitcoin_api = bitcoin_api.json()
        return bitcoin_api


def destination(bitcoin_api):
    print(
        "\n< The plane just arrived in the Philippines >"
        "\n< You open your phone to check your Bitcoin balance >"
    )
    crypto(bitcoin_api)
    print(
        "\n< A local student researcher approached your group >"
        "\n< He asks for you to answer a math literacy quiz >"
        "\n< You take the quiz to help them with their study >"
    )
    quiz()


def crypto(bitcoin_api):
    balance = float(sys.argv[1])
    bitcoin_usd = float(bitcoin_api["data"].get("priceUsd"))
    usd_balance = balance * bitcoin_usd
    print(f"\nBalance:  {balance:,.4f}")
    print(f"In USD:   ${usd_balance:,.4f}")


def quiz():
    max_level = 3
    user_level = get_level(max_level)
    random.seed(user_level)

    problems = 10
    minimum, maximum = 0, 42
    correct = 0

    for _ in range(problems):
        x = random.randint(minimum, maximum)
        y = random.randint(minimum, maximum)
        answer = x + y
        lives = 3

        print()
        while True:
            if lives == 0:
                break
            print(
                f"Lives:    {convert_life(lives)}"
                f"\nSystem:   {x} + {y}?"
            )
            try:
                user_answer = int(input("User:     ").strip())
            except ValueError:
                lives -= 1
            else:
                if user_answer == answer:
                    correct += 1
                    break
                lives -= 1
    
    print(f"Score:    {correct}/{problems}")
            

def convert_life(lives):
    heart = emoji.emojize(":blue_heart:")
    hearts = []
    for _ in range(lives):
        hearts.append(heart)
    return "".join(hearts)
                

if __name__ == "__main__":
    main()