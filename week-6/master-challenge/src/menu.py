

import sys
from src.count import retrieve_file


def show_menu():
    file = retrieve_file()
    if not file:
        print("[Error  :  System] No csv file selected.")
        sys.exit(1)