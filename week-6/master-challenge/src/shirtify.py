

from utils import args
from utils import validation as val


def shirtify():
    imgs_path, imgs_list = val.access_dir("images")
    old_file, ext = args.validate_file(2, 4, [".jpg", ".jpeg", ".png"], True, True, imgs_list)
    new_file = args.validate_file(3, 4, [ext], False, False, imgs_list)