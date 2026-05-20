

import re


def check_ip():
    while True:
        print("[Prompt - System] Enter IPv4 address.")
        ip = input(">>> ").strip()

        if re.search(r"^(((?:[0-9]){1})|((?:[1-9]){1}(?:[0-9]){1}))$", ip):
            print("Valid")
        else:
            print("Invalid")