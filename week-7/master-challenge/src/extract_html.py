

import re


def extract_html():
    print("[Prompt - System] Enter Youtube HTML:")
    user_html = input(">>> ").strip()

    if src := re.search("^<iframe .*src=\"https://www.youtube.com/embed/(.{11})\" *.*></iframe>$", user_html):
        print(src.group(1))