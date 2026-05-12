

import sys
from utils import validation as val


def show_menu():
    file = val.retrieve_file()
    if not file:
        print("[Error  :  System] No csv file selected.")
        sys.exit(1)
    
    valid_file = val.validate_file(file, ".csv")
    if not valid_file:
        print("[Error  :  System] Invalid file.")
        sys.exit(1)

    csvs_path, csvs_list = val.access_samples("csvs")