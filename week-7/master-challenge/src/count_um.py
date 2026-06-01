

from utils.filter import filter_all


def count_um():
    print("[Prompt - System] Enter text:")
    input_ = input(">>> ").strip()
    condition = r"\bum\b"

    um_list = filter_all(condition, input_)
    ums = len(um_list)
    print(f"[Success - System] Total ums: {ums}")