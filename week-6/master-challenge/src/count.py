

import sys


def count_lines():
    file = retrieve_file()
    if not file:
        print("[Error  :  System] No python program selected.")
        sys.exit()
    program = validate_file(file)
    if not program:
        print("[Error  :  System] Invalid file.")
        sys.exit()


def retrieve_file():
    try:
        file = sys.argv[2]
    except IndexError:
        return None
    else:
        return file
    

def validate_file(program):
    if not program.endswith(".py"):
        return None
    return program