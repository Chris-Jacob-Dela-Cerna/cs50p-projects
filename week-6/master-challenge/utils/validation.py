

import os
import sys


def retrieve_sys(idx):
    try:
        file = sys.argv[idx]
    except IndexError:
        return None
    else:
        return file


def validate_extension(file, extensions):
    for ext in extensions:
        if file.endswith(ext):
            return file, ext
    return None, None


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