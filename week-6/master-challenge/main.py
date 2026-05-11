

import sys
from src.count import count_lines
from src.menu import show_menu
from src.reformat import reformat_names
from src.shirtify import shirtify


def main():
    try:
        mode = sys.argv[1]
    except IndexError:
        print("[Error  :  System] No mode selected.")
        sys.exit(1)

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