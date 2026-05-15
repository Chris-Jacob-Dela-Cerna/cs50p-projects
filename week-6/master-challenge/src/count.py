

import os
from utils import args
from utils import validation as val


def count_lines():
    smpls_path, smpls_list = val.access_dir("samples")
    program = args.validate_file(2, 3, [".py"], False, True, smpls_list)

    prgm_path = os.path.join(smpls_path, program)

    file = read_lines(prgm_path)
    lines = filter_lines(file)
    num = len(lines)
    
    print(f"[Success:  System] Total line count: {num}")


def read_lines(path):
    with open(path, "r") as file:
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