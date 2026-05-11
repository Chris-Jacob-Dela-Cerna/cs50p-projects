

import os
import sys


def count_lines():
    file = retrieve_file()
    if not file:
        print("[Error  :  System] No python program selected.")
        sys.exit()

    smpls_path, smpls_list = access_samples()
    
    program = validate_file(file)
    if not program:
        print("[Error  :  System] Invalid file.")
        sys.exit()


def access_samples():
    src_path = os.path.dirname(os.path.abspath(__file__))
    root_path = os.path.dirname(src_path)
    smpls_path = os.path.join(root_path, "data", "samples")
    os.makedirs(smpls_path, exist_ok=True)
    smpls_list = os.listdir(smpls_path)
    return smpls_path, smpls_list


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