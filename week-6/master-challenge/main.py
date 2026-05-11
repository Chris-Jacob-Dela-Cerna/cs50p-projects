

import sys


def main():
    try:
        mode = sys.argv[1]
    except IndexError:
        print("[Error  :  System] No mode selected.")
    else:
        match mode:
            case "count":
                pass
            case "menu":
                pass
            case "reformat":
                pass
            case "shirtify":
                pass
            case _:
                print("[Error  :  System] Invalid mode.")


if __name__ == "__main__":
    main()