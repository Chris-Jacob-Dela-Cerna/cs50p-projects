# Document: This python is my last application of CS50P Week 4.

import sys
import requests



def main():
    if check_net():
        print("System:   [Connection timeout]")
        sys.exit()
    print("System:   [Connection established]")

    if check_args() == 0:
        pass
    elif check_args() == 1:
        pass
    else:
        pass

def check_net():
    try:
        bitcoin_api = requests.get(
            "https://rest.coincap.io/v3/assets/bitcoin?apiKey=ac615c2394516854ececfaa073631bf60b40a36236294c491470d41a0770595a"
            )
        bitcoin_api.raise_for_status()
    except requests.RequestException:
        return True


def check_args():
    pass


if __name__ == "__main__":
    main()