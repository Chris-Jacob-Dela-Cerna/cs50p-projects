

import re


def extract_html():
    print("[Prompt - System] Enter Youtube HTML:")
    user_html = input(">>> ").strip()

    if src := re.search(r"^<iframe .*src=\"https?://(?:www\.)?youtube.com/embed/(.{11})\" *.*></iframe>$", user_html):
        print(src.group(1))
    else:
        print("[Error  - System] Invalid HTML format.")