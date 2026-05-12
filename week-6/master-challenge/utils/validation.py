

import os
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


def access_samples(data_dir):
    src_path = os.path.dirname(os.path.abspath(__file__))
    root_path = os.path.dirname(src_path)
    cpath = os.path.join(root_path, "data", data_dir)
    os.makedirs(cpath, exist_ok=True)
    clist = os.listdir(cpath)
    return cpath, clist