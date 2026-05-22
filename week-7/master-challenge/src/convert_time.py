

import re


def convert_time():
    print("[Prompt - System] Enter time:")
    user_time = input(">>> ").strip()

    if time := re.search(r"^([0-9](?::[0-9]{2})) to ([0-9](?::[0-9]{2}))$", user_time):
        print(time.group(1), time.group(2))