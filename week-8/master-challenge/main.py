

import sys
from src.age import age
from utils.get_sys import get_sys


def main():
    mode = get_sys(1, "[Error  - System] Please enter a mode.")
    
    modes = {
        "age": age,
    }

    if mode not in modes:
        sys.exit("[Error  - System] Invalid mode.")

    modes[mode]()
    

if __name__ == "__main__":
    main()