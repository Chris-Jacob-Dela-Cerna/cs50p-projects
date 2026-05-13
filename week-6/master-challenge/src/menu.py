

import os
from utils import io
from utils import validation as val


def show_menu():
    file = val.retrieve_file(2)
    if not file: 
        io.abort("No file selected.")
    
    valid_file = val.validate_extension(file, ".csv")
    if not valid_file:
        io.abort("Invalid file.")

    csvs_path, csvs_list = val.access_dir("csvs")

    program = val.check_file(valid_file, csvs_list)
    if not program:
        io.abort("File does not exist.")
    
    prgm_path = os.path.join(csvs_path, program)