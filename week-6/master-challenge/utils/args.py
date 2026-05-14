

from utils import io
from utils import validation as val


def validate_file(idx, ext, must_exist, list_):
    file = val.retrieve_sys(idx)
    if not file:
        io.abort("No file selected.")

    valid_file_ext = val.validate_extension(file, ext)
    if not valid_file_ext:
        io.abort("Invalid file.")

    valid_file = val.check_file(valid_file_ext, list_)
    if must_exist:
        if not valid_file:
            io.abort("File does not exist.")
    else:
        if valid_file:
            io.abort("File already exists.")
        
    return valid_file