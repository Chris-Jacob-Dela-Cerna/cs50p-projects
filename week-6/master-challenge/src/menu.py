

import sys
from utils import validation as val


def show_menu():
    file = val.retrieve_file()
    if not file:
        print("[Error  :  System] No file selected.")
        sys.exit(1)
    
    valid_file = val.validate_extension(file, ".csv")
    if not valid_file:
        print("[Error  :  System] Invalid file.")
        sys.exit(1)

    csvs_path, csvs_list = val.access_dir("csvs")

    program = val.check_file(valid_file, csvs_list)
    if not program:
        print("[Error  :  System] File does not exist.")
        sys.exit(1)