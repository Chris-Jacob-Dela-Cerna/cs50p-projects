

from utils import args
from utils import io
from utils import validation as val


def reformat_names():
    if val.retrieve_sys(4):
        io.abort("Too many arguments.")
    csvs_path, csvs_list = val.access_dir("csvs")
    old_file = args.validate_file(2, ".csv", True, csvs_list)
    new_file = args.validate_file(3, ".csv", False, csvs_list)