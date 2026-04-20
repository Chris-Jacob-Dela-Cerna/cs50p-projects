# Document: This python is my last application of CS50P Week 4.

import sys
import requests

api_key = "secret"


def main():
    if check_net():
        sys.exit()
    if check_args():
        sys.exit()


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
        
        


def check_args():
    try:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            return # 
        elif sys.argv[1].isdigit():
            return # 
        else:
            raise IndexError
    except IndexError:
        print("System:   Invalid command-line argument.")
        return True


if __name__ == "__main__":
    main()