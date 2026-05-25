

from utils.abort import abort
from utils.filter import filter_


def extract_html():
    print("[Prompt - System] Enter Youtube HTML:")
    input_ = input(">>> ").strip()
    condition = r"^<iframe .*src=\"(https?://(?:www\.)?)youtube.com/embed/(.{11})(?:\?si=)?[a-zA-Z0-9]*\" *.*></iframe>$"

    if not (src := filter_(condition, input_)):
        abort("Invalid HTML format.")
    
    src_list = src.groups()
    print(f"[Success - System] {src_list[0]}youtu.be/{src_list[1]}")