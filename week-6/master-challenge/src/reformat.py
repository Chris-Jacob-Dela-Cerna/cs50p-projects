

import csv
import os
from utils import args
from utils import validation as val


def reformat_names():
    csvs_path, csvs_list = val.access_dir("csvs")
    old_file = args.validate_file(2, 4, [".csv"], False, True, csvs_list)
    new_file = args.validate_file(3, 4, [".csv"], False, False, csvs_list)

    old_path = os.path.join(csvs_path, old_file)
    new_path = os.path.join(csvs_path, new_file)

    formatted = reformat(old_path)
    import_to_file(new_path, formatted)

    print(f"[Success:  System] File successfully formatted.")


def reformat(path):
    with open(path, "r") as file:
        reader = csv.DictReader(file)
        formatted = []
        for row in reader:
            last, first = row["name"].split(", ")
            affiliation = row["affiliation"]
            formatted.append({"First Name": first, "Last Name": last, "Affiliation": affiliation})
    return formatted


def import_to_file(path, formatted):
    with open(path, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["First Name", "Last Name", "Affiliation"])
        writer.writeheader()
        writer.writerows(formatted)