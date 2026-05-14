

import csv
import os
from utils import args
from utils import validation as val


def reformat_names():
    csvs_path, csvs_list = val.access_dir("csvs")
    old_file = args.validate_file(2, 4, ".csv", True, csvs_list)
    new_file = args.validate_file(3, 4, ".csv", False, csvs_list)

    old_path = os.path.join(csvs_path, old_file)
    new_path = os.path.join(csvs_path, new_file)

    with open(old_path, "r") as old:
        reader = csv.DictReader(old)
        formatted = []
        for row in reader:
            last, first = row["name"].split(", ")
            affiliation = row["affiliation"]
            formatted.append({"First Name": first, "Last Name": last, "affiliation": affiliation})
    return formatted