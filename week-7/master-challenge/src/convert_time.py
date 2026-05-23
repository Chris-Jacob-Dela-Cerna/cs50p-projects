

from utils.abort import abort
from utils.filter import filter_


def convert_time():
    print("[Prompt - System] Enter time:")
    input_ = input(">>> ").strip()
    condition = r"^([0-9]{1,2}(?::[0-9]{2})?) (AM|PM) to ([0-9]{1,2}(?::[0-9]{2})?) (AM|PM)$"

    if not (time_list := filter_(condition, input_)):
        abort("Invalid time format.")

    hour1, minute1 = extract_time(time_list[0])
    hour2, minute2 = extract_time(time_list[2])

    check_hour(hour1)
    check_hour(hour2)
    check_minute(minute1)
    check_minute(minute2)

    period1 = time_list[1]
    period2 = time_list[3]


def extract_time(time):
    if ":" in time:
        hour, minute = time.split(":")
        return int(hour), int(minute)
    return int(time), 0


def check_hour(hour):
    if hour < 1 or hour > 12:
        abort(f"Invalid hour range ({hour}).")


def check_minute(minute):
    if minute > 59:
        abort(f"Invalid minute range ({minute}).")