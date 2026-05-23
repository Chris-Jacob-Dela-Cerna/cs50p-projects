

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
        hour, minute = time1.split(":")
        hour1 = int(hour)
        minute1 = int(minute)
    else:
        hour1 = int(time1)
        minute1 = 0

    if 1 > hour1 > 12 or 1 > hour1 > 12:
        abort("Invalid hour range.")

    if ":" in time2:
        hour, minute = time2.split(":")
        hour2 = int(hour)
        minute2 = int(minute)
    else:
        hour2 = int(time2)
        minute2 = 0

    if 1 > hour2 > 12 or 1 > hour2 > 12:
        abort("Invalid hour range.")

    