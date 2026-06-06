# Document: This python is my last application of CS50P Week 8.

import sys
from src.get_age import get_age
from src.store_cookie import store_cookie
from utils.get_sys import get_sys


def main():
    mode = get_sys(1, "Please enter a mode.")

    modes = {
        "age": get_age,
        "jar": store_cookie,
    }
    if mode not in modes:
        sys.exit("[Error  - System] Invalid mode.")

    modes[mode]()


if __name__ == "__main__":
    main()