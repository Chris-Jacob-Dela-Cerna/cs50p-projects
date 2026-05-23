

from utils.abort import abort
from utils.filter import filter_


def convert_time():
    print("[Prompt - System] Enter time:")
    input_ = input(">>> ").strip()
    condition = r"^([0-9](?::[0-9]{2})?) (AM|PM) to ([0-9](?::[0-9]{2})?) (AM|PM)$"

    if not (time_list := filter_(condition, input_)):
        abort("Invalid time format.")

    time1 = time_list[0]
    meridiem1 = time_list[1]
    time2 = time_list[2]
    meridiem2 = time_list[3]

    if ":" in time1:
        hour1, minute1 = time1.split(":")
        hour1 = int(hour1)
    if 1 > hour1 > 12 or 1 > hour1 > 12:
        abort("Invalid hour range.")
    if ":" in time2:
        hour2, minute2 = time2.split(":")
        hour2 = int(hour2)
    if 1 > hour2 > 12 or 1 > hour2 > 12:
        abort("Invalid hour range.")

    