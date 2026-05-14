

from utils import io
from utils import validation as val


def validate_file(idx, extra, extensions, must_exist, list_):
    file = val.retrieve_sys(idx)
    if not file:
        io.abort("No file selected.")
    
    if val.retrieve_sys(extra):
        io.abort("Too many arguments.")

    valid_ext, ext = val.validate_extension(file, extensions)
    if not valid_ext:
        io.abort("Invalid file.")

    valid_file = val.check_file(valid_ext, list_)
    if must_exist:
        if not valid_file:
            io.abort("File does not exist.")
    else:
        if valid_file:
            io.abort("File already exists.")

    return file