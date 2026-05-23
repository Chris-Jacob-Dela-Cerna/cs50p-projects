

from utils.abort import abort
from utils.filter import filter_


def convert_time():
    print("[Prompt - System] Enter time:")
    input_ = input(">>> ").strip()
    condition = r"^([0-9](?::[0-9]{2})?) (AM|PM) to ([0-9](?::[0-9]{2})?) (AM|PM)$"

    if not (time_list := filter_(condition, input_)):
        abort("Invalid time format.")

    list_ = [idx for idx in time_list]
    print(list_)