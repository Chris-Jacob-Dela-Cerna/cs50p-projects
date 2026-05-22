

import re
import sys


def check_ip():
    print("[Prompt - System] Enter IPv4 address:")
    user_ip = input(">>> ").strip()

    if ip := re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", user_ip):
        for ipnum in ip.groups():
            if not validate_number(ipnum):
                print(f"[Error  - System] Invalid IP number ({ipnum}).")
                sys.exit(1)
        print("[Success - System] Valid IPv4 address.")
    else:
        print("[Error  - System] Invalid IPv4 format.")
        sys.exit(1)


def validate_number(number):
    if 0 > int(number) or int(number) > 255:
        return False
    return True