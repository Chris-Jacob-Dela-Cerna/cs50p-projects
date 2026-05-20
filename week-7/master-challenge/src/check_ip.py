

import re


def check_ip():
    while True:
        print("[Prompt - System] Enter IPv4 address.")
        ip = input(">>> ").strip()

        if re.search(r"^(((?:[0-9]){1})|((?:[1-9]){1}(?:[0-9]){1})|((?:[1]){1}(?:[0-9]){2})|((?:[2]){1}(?:[0-4]){1}(?:[0-9]){1})|((?:[2]){1}(?:[5]){1}(?:[0-5]){1}))$", ip):
            print("Valid")
        else:
            print("Invalid")