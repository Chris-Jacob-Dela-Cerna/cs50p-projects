

import re


# https://www.instagram.com/username/

while True:
    url = input("Enter your Instagram URL: ").strip()

    if matches := re.search(r"^(?:https?://|)(?:www\.|)instagram\.com/(\w+)/?$", url):
        print(f"[Success:  System] Your username is {matches.group(1)}.")
    else:
        print("[Fail   :  System] Please enter a valid URL.")