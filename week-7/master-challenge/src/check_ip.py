

import re
import sys


def check_ip():
    print("[Prompt - System] Enter IPv4 address.")
    user_ip = input(">>> ").strip()

    if ip := re.search(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", user_ip):
        pass
    else:
        print("[Error  - System] Invalid IPv4 format.")
        sys.exit()