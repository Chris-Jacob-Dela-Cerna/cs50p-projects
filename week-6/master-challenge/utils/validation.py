

import os
import sys


def retrieve_file():
    try:
        file = sys.argv[2]
    except IndexError:
        return None
    else:
        return file


def validate_extension(file, extension):
    if not file.endswith(extension):
        return None
    return file


def access_dir(data_dir):
    src_path = os.path.dirname(os.path.abspath(__file__))
    root_path = os.path.dirname(src_path)
    path = os.path.join(root_path, "data", data_dir)
    os.makedirs(path, exist_ok=True)
    list_ = os.listdir(path)
    return path, list_


def check_file(file, list_):
    if file not in list_:
        return None
    return file