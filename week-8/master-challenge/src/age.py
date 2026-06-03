

import re
import sys
from utils.get_sys import get_sys


def age():
    birth_date = get_sys(2, "[Error  - System] Please enter a birthdate in this format: YYYY-MM-DD")
    if not (bd := re.search(r"^([0-9]{4})-([0-9]{2})-([0-9]{2})$", birth_date)):
        sys.exit("[Error  - System] Please use the right format: YYYY-MM-DD")