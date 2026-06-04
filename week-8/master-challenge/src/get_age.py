

import datetime as dt
import inflect
import re
import sys
from utils.get_sys import get_sys


def get_age():
    birth_date = get_sys(2, "Please enter a birthdate in this format: YYYY-MM-DD")
    if not (bd := re.search(r"^([0-9]{4})-([0-9]{2})-([0-9]{2})$", birth_date)):
        sys.exit("[Error  - System] Please use the right format: YYYY-MM-DD")

    try:
        b_date = dt.date(int(bd[1]), int(bd[2]), int(bd[3]))
    except ValueError as ve:
        sys.exit(f"[Error  - System] {str(ve).capitalize()}.")

    today = dt.date.today()
    date = today - b_date
    minutes = round(date.total_seconds() / 60)

    p = inflect.engine()
    words = p.number_to_words(minutes, andword="")
    print(f"You are {words} years old.")