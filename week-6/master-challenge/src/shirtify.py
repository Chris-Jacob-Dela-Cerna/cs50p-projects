

import os
from PIL import Image
from PIL import ImageOps
from utils import args
from utils import validation as val


def shirtify():
    imgs_path, imgs_list = val.access_dir("images")
    old_file, ext = args.validate_file(2, 5, [".jpg", ".jpeg", ".png"], True, True, imgs_list)
    new_file = args.validate_file(3, 5, [ext], False, False, imgs_list)
    shirt_file = args.validate_file(4, 5, ["shirt_.png"], False, True, imgs_list)

    old_path = os.path.join(imgs_path, old_file)
    new_path = os.path.join(imgs_path, new_file)
    shirt_path = os.path.join(imgs_path, shirt_file)

    old = Image.open(old_path)
    shirt = Image.open(shirt_path)
    old.paste(shirt)
    