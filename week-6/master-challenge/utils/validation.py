

import sys


def retrieve_file():
    try:
        file = sys.argv[2]
    except IndexError:
        return None
    else:
        return file
    

def validate_file(file, extension):
    if not file.endswith(extension):
        return None
    return file