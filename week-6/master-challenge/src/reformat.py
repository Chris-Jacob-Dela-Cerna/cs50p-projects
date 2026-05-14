

from utils import args
from utils import validation as val


def reformat_names():
    csvs_path, csvs_list = val.access_dir("csvs")
    old_file = args.validate_file(2, 4, ".csv", True, csvs_list)
    new_file = args.validate_file(3, 4, ".csv", False, csvs_list)