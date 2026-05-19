# RegEx scratch file - practicing regular expressions, syntax, and logic

import re


def main():
    pass

""" 
Accepted variations: 
https://www.instagram.com/username/
http://www.instagram.com/username/
www.instagram.com/username/
instagram.com/username/
instagram.com/username
"""

def instagram_login():
    while True:
        url = input("Enter your Instagram URL: ").strip()

        if matches := re.search(r"^(?:https?://|)(?:www\.|)instagram\.com/(\w+)/?$", url):
            print(f"[Success:  System] Your username is {matches.group(1)}.")
        else:
            print("[Fail   :  System] Please enter a valid URL.")


def color_code():
    pass


main()