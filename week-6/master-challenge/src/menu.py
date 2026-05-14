

import csv
import os
import tabulate as tb
from utils import args
from utils import validation as val


def show_menu():
    csvs_path, csvs_list = val.access_dir("csvs")
    file = args.validate_file(2, 3, [".csv"], True, csvs_list)

    prgm_path = os.path.join(csvs_path, file)
    header, table = extract_table_data(prgm_path)

    print(tb.tabulate(table, header, tablefmt="grid"))


def extract_table_data(path):
    with open(path, "r") as file:
        reader = csv.reader(file)
        table = []
        for idx, line in enumerate(reader):
            if idx == 0:
                header = line
            else:
                table.append(line)
    return header, table