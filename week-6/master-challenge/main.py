

import sys


def main():
    try:
        mode = sys.argv[1]
    except IndexError:
        print("[Error  :  System] No mode selected.")
    else:
        pass


if __name__ == "__main__":
    main()