

from utils.abort import abort
from utils.filter import filter_


def check_ip():
    print("[Prompt - System] Enter IPv4 address:")
    input_ = input(">>> ").strip()
    condition = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"

    if not (ipnum_list := filter_(condition, input_)):
        abort("Invalid IPv4 format.")

    if not check_ip_number(ipnum_list.groups()):
        abort(f"Invalid IP number.")

    print("[Success - System] Valid IPv4 address.")


def check_ip_number(list_):
    for num in list_:
        if int(num) > 255:
            return False
    return True