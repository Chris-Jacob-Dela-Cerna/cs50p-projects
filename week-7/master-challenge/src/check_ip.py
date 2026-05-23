

from utils.abort import abort
from utils.filter import filter_


def check_ip():
    print("[Prompt - System] Enter IPv4 address:")
    input_ = input(">>> ").strip()
    condition = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"

    if not (ipnum_list := filter_(condition, input_)):
        abort("Invalid IPv4 format.")

    for ipnum in ipnum_list:
        if not validate_number(ipnum):
            abort(f"Invalid IP number ({ipnum}).")

    print("[Success - System] Valid IPv4 address.")


def validate_number(number):
    if not (0 > int(number) or int(number) > 255):
        return True