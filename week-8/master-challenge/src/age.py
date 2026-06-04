

import datetime as dt
import inflect
import re
import sys
from utils.get_sys import get_sys


def get_age():
    birth_date = get_sys(2, "[Error  - System] Please enter a birthdate in this format: YYYY-MM-DD")
    if not (bd := re.search(r"^([0-9]{4})-([0-9]{2})-([0-9]{2})$", birth_date)):
        sys.exit("[Error  - System] Please use the right format: YYYY-MM-DD")

    try:
        b_date = dt.date(int(bd[1]), int(bd[2]), int(bd[3]))
    except ValueError as ve:
        sys.exit(f"[Error  - System] {str(ve).title()}.")

    today = dt.date.today()
    date = today - b_date
    age = re.search(r"^([0-9]*) days?, 0:00:00$", str(date))
    days = dt.timedelta(days=int(age.group(1)))
    minutes = round(days.total_seconds() / 60)
    print(minutes)