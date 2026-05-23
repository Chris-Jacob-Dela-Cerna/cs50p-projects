

from utils.abort import abort
from utils.filter import filter_


def extract_html():
    print("[Prompt - System] Enter Youtube HTML:")
    input_ = input(">>> ").strip()
    condition = r"^<iframe .*src=\"(https?://(?:www\.)?)youtube.com/embed/(.{11})\" *.*></iframe>$"

    if src := filter_(condition, input_):
        print(f"[Success - System] {src[1]}youtu.be/{src[2]}")
    else:
        abort("Invalid HTML format.")