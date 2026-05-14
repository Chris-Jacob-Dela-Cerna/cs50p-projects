

import os
from utils import io
from utils import validation as val


def count_lines():
    smpls_path, smpls_list = val.access_dir("samples")
    program = validate_file(2, ".py", smpls_list)

    prgm_path = os.path.join(smpls_path, program)
    file = read_lines(prgm_path)
    lines = filter_lines(file)
    num = count(lines)

    print(f"[Success:  System] Total line count: {num}")


def validate_file(idx, ext, list_):
    file = val.retrieve_sys(idx)
    if not file:
        io.abort("No file selected.")

    if val.retrieve_sys(idx + 1):
        io.abort("Too many arguments.")

    valid_file_ext = val.validate_extension(file, ext)
    if not valid_file_ext:
        io.abort("Invalid file.")

    valid_file = val.check_file(valid_file_ext, list_)
    if not valid_file:
        io.abort("File does not exist.")
    return valid_file


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