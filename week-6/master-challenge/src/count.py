

import os
import sys
from utils import validation as val


def count_lines():
    file = val.retrieve_file(2)
    if not file:
        print("[Error  :  System] No file selected.")
        sys.exit(1)
    
    valid_file = val.validate_extension(file, ".py")
    if not valid_file:
        print("[Error  :  System] Invalid file.")
        sys.exit(1)

    smpls_path, smpls_list = val.access_dir("samples")

    program = val.check_file(valid_file, smpls_list)
    if not program:
        print("[Error  :  System] File does not exist.")
        sys.exit(1)

    prgm_path = os.path.join(smpls_path, program)
    file = read_lines(prgm_path)
    lines = filter_lines(file)
    num = count(lines)

    print(f"[Success:  System] Total line count: {num}")


def read_lines(prgm_path):
    with open(prgm_path, "r") as file:
        reader = file.readlines()
        return reader


def filter_lines(file):
    new_file = []
    for line in file:
        if line.strip() == "":
            continue
        elif line.strip().startswith("#"):
            continue
        new_file.append(line)
    return new_file


def count(lines):
    total = 0
    for _ in lines:
        total += 1
    return total