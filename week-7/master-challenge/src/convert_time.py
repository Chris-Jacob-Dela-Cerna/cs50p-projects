

from utils.abort import abort
from utils.filter import filter_


def convert_time():
    print("[Prompt - System] Enter time:")
    input_ = input(">>> ").strip()
    condition = r"^([0-9](?::[0-9]{2})?) (AM|PM) to ([0-9](?::[0-9]{2})?) (AM|PM)$"

    if not (time_list := filter_(condition, input_)):
        abort("Invalid time format.")

    hour1, minute1 = extract_time(time_list[0])
    hour2, minute2 = extract_time(time_list[2])

    if 1 > hour1 > 12 or 1 > hour2 > 12:
        abort("Invalid hour range.")
    if minute1 > 59 or minute2 > 59:
        abort("Invalid minute range.")

    period1 = time_list[1]
    period2 = time_list[3]


def extract_time(time):
    if ":" in time:
        hour, minute = time.split(":")
        return int(hour), int(minute)
    return int(time), 0