# Document: This python is my last application of CS50P Week 6.

import sys
from src.count import count_lines
from src.menu import show_menu
from src.reformat import reformat_names
from src.shirtify import shirtify
from utils import io
from utils import validation as val


def main():
    mode = val.retrieve_sys(1)
    if not mode:
        io.abort("No mode selected.")

    modes = {
        "count": count_lines,
        "menu": show_menu,
        "reformat": reformat_names,
        "shirtify": shirtify,
    }

    if mode not in modes:
        print("[Error  :  System] Invalid mode.")
        sys.exit(1)
    modes[mode]()


if __name__ == "__main__":
    main()