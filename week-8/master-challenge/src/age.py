

import datetime as dt
import inflect
import re
import sys
from utils.get_sys import get_sys


def age():
    birth_date = get_sys(2, "[Error  - System] Please enter a birthdate in this format: YYYY-MM-DD")
    if not (bd := re.search(r"^([0-9]{4})-([0-9]{2})-([0-9]{2})$", birth_date)):
        sys.exit("[Error  - System] Please use the right format: YYYY-MM-DD")

    b_year = int(bd[1])
    b_month = int(bd[2])
    b_day = int(bd[3])
    today = dt.date.today()
    age = today - dt.date(b_year, b_month, b_day)
    print(age)