

import re


def convert_time():
    print("[Prompt - System] Enter time:")
    user_time = input(">>> ").strip()

    if time := re.search(r"^([0-9](?::[0-9]{2})?) (AM|PM) to ([0-9](?::[0-9]{2})?) (AM|PM)$", user_time):
        print(time.groups())
    else:
        print("[Error  - System] Invalid time format.")