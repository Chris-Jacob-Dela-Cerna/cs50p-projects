

import sys
from src.age import age


def main():
    try:
        mode = sys.argv[1]
    except IndexError:
        sys.exit("[Error  - System] Please enter a mode.")
    
    modes = {
        "age": age,
    }

    if mode not in modes:
        sys.exit("[Error  - System] Invalid mode.")

    modes[mode]()
    

if __name__ == "__main__":
    main()