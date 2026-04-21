# Document: This python is my last application of CS50P Week 4.

import sys
import requests
import pyfiglet

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
            f"\n          >>> python {sys.argv[0]} [input] <<<"
        )


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
    

def airport():
    identity_banner()


def identity_banner():
    try:
        if sys.argv[2] not in figlet_fonts:
            raise IndexError
    except IndexError:
        print(
            "System:   Invalid command-line argument."
            f"\n          >>> python {sys.argv[0]} {sys.argv[1]} [input] <<<"
        )


def destination():
    print("Destination")


if __name__ == "__main__":
    main()