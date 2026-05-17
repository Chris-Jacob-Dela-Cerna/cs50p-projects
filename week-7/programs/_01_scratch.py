

import re


# https://www.instagram.com/username/

while True:
    url = input("Enter your Instagram URL: ").strip()

    if re.search(r"^(?:https?://|)(?:www\.|)instagram\.com/\w+/?$", url):
        print("[Success:  System]")
    else:
        print("[Fail   :  System]")