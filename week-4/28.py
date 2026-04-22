# Document: This python is my last application of CS50P Week 4.

import sys
import requests
import pyfiglet
import emoji

api_key = "secret"
figlet_fonts = pyfiglet.FigletFont.getFonts()


def main():
    arg_result = check_args()
    if arg_result == 0:
        airport()
    elif arg_result == 1:
        if check_net():
            sys.exit()
        destination()
    else:
        sys.exit()
        
        
def check_args():
    try:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            return 0
        elif sys.argv[1].isdigit():
            return 1 
        else:
            raise IndexError
    except IndexError:
        print(
            "System:   Invalid command-line argument."
            f"\n          >>> python {sys.argv[0]} [input]"
        )


def airport():
#    if check_font():
#        sys.exit()
#    identity_banner()
    review()


def check_font():
    try:
        if sys.argv[2] not in figlet_fonts:
            raise IndexError
    except IndexError:
        print(
            "System:   Invalid command-line argument."
            f"\n          >>> python {sys.argv[0]} {sys.argv[1]} [input]"
        )
        return True

        
def identity_banner():
    print(
        "\n< While waiting for your plane at the airport, you spot a font dashboard >"
        "\n< The dashboard lets you enter text and convert it into the font you selected >"
    )
    user_text = input("\nUser:     ").strip()
    header = pyfiglet.figlet_format("Welcome Traveller!", font="mini")
    message = pyfiglet.figlet_format(user_text, font=sys.argv[2])
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

def check_net():
    try:
        bitcoin_api = requests.get(
            "https://rest.coincap.io/v3/assets/bitcoin?apiKey=", api_key
            )
        bitcoin_api.raise_for_status()
    except requests.RequestException:
        print("System:   [Connection timeout]")
        return True
    else:
        print("System:   [Connection established]")


def destination():
    print("Destination")


if __name__ == "__main__":
    main()