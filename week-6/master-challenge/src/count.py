

import os
from utils import io
from utils import validation as val


def count_lines():
    file = val.retrieve_sys(2)
    if not file:
        io.abort("No file selected.")

    extra = val.retrieve_sys(3)
    if extra:
        io.abort("Too many arguments.")
    
    valid_file = val.validate_extension(file, ".py")
    if not valid_file:
        io.abort("Invalid file.")

    smpls_path, smpls_list = val.access_dir("samples")

    program = val.check_file(valid_file, smpls_list)
    if not program:
        io.abort("File does not exist.")

    prgm_path = os.path.join(smpls_path, program)
    file = read_lines(prgm_path)
    lines = filter_lines(file)
    num = count(lines)

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


def count(lines):
    total = 0
    for _ in lines:
        total += 1
    return total