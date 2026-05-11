

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
    else:
        match mode:
            case "count":
                count_lines()
            case "menu":
                show_menu()
            case "reformat":
                reformat_names()
            case "shirtify":
                shirtify()
            case _:
                print("[Error  :  System] Invalid mode.")


if __name__ == "__main__":
    main()