

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
    check_time(hour1, minute1)
    check_time(hour2, minute2)

    period1 = time_list[1]
    period2 = time_list[3]
    hour1 = convert_hour(period1, hour1)
    hour2 = convert_hour(period2, hour2)

    print(f"[Success - System] Time: {hour1}:{minute1:02d} to {hour2}:{minute2:02d}.")


def extract_time(time):
    if ":" in time:
        hour, minute = time.split(":")
        return int(hour), int(minute)
    return int(time), 0


def check_time(hour, minute):
    if hour < 1 or hour > 12:
        abort(f"Invalid hour range ({hour}).")
    if minute > 59:
        abort(f"Invalid minute range ({minute}).")


def convert_hour(period, hour):
    if period == "AM":
        if hour == 12:
            return 0
        return hour
    else:
        return hour + 12