

import re


def check_ip():
    while True:
        print("[Prompt - System] Enter IPv4 address.")
        user_ip = input(">>> ").strip()

        if re.search(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", user_ip):
            print("Valid")