

import sys
from utils.abort import abort
from utils.filter import filter_


def check_ip():
    print("[Prompt - System] Enter IPv4 address:")
    input_ = input(">>> ").strip()
    condition = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"

    if ipnum_list := filter_(condition, input_):
        for item in ipnum_list.groups():
            if not validate_number(item):
                print(f"[Error  - System] Invalid IP number ({item}).")
                sys.exit(1)
        print("[Success - System] Valid IPv4 address.")
    else:
        abort("Invalid IPv4 format.")


def validate_number(number):
    if 0 > int(number) or int(number) > 255:
        return False
    return True