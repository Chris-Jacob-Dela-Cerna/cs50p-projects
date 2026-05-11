

import os
import sys


def count_lines():
    file = retrieve_file()
    if not file:
        print("[Error  :  System] No python program selected.")
        sys.exit(1)

    smpls_path, smpls_list = access_samples()
    
    valid_file = validate_file(file)
    if not valid_file:
        print("[Error  :  System] Invalid file.")
        sys.exit(1)

    program = check_file(valid_file, smpls_list)
    if not program:
        print("[Error  :  System] File does not exist.")
        sys.exit(1)

    prgm_path = os.path.join(smpls_path, program)
    file = read_lines(prgm_path)
    lines = extract_text(file)

    for line in lines:
        print(line, end="")


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


def validate_file(file):
    if not file.endswith(".py"):
        return None
    return file


def check_file(file, smpls_list):
    if file not in smpls_list:
        return None
    return file


def read_lines(prgm_path):
    with open(prgm_path, "r") as file:
        reader = file.readlines()
        return reader


def extract_text(file):
    new_file = []
    for line in file:
        if line.strip() == "":
            continue
        elif line.strip().startswith("#"):
            continue
        new_file.append(line)
    return new_file