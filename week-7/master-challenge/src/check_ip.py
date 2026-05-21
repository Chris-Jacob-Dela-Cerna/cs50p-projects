

import re
import sys


def check_ip():
    print("[Prompt - System] Enter IPv4 address:")
    user_ip = input(">>> ").strip()

    if ip := re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", user_ip):
        for number in ip.groups():
            if not validate_number(number):
                print(f"[Error  - System] Invalid IP number ({number}).")
    else:
        print("[Error  - System] Invalid IPv4 format.")
        sys.exit()


def validate_number(number):
    if 0 > int(number) or int(number) > 255:
        return False
    return True 