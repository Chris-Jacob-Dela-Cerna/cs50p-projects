

import sys
from src.get_age import get_age
from src.store_cookie import store_cookie
from utils.get_sys import get_sys


def main():
    mode = get_sys(1, "[Error  - System] Please enter a mode.")

    modes = {
        "age": get_age,
        "jar": store_cookie,
    }
    if mode not in modes:
        sys.exit("[Error  - System] Invalid mode.")

    modes[mode]()
    

if __name__ == "__main__":
    main()