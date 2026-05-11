

import sys


def count_lines():
    try:
        program = sys.argv[2]
    except IndexError:
        print("[Error  :  System] No python program selected.")
    else:
        if not program.endswith(".py"):
            print("[Error  :  System] Invalid file.")
            sys.exit()