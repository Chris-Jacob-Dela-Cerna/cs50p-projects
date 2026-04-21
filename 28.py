# Document: This python is my last application of CS50P Week 4.

import sys
import requests

api_key = "secret"


def main():
    arg_result = check_args()
    if arg_result == 0:
        airport()
    if arg_result == 1:
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
        print("System:   Invalid command-line argument.")


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
    print("Airport")


def destination():
    print("Destination")


if __name__ == "__main__":
    main()