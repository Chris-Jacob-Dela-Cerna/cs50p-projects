

import sys


def main():
    try:
        mode = sys.argv[1]
    except IndexError:
        print("[Error  - System] No modes selected.")
        sys.exit()

    


if __name__ == "__main__":
    main()