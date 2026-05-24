

from utils.abort import abort
from utils.filter import filter_all


def count_um():
    print("[Prompt - System] Enter text:")
    input_ = input(">>> ").strip()
    condition = r"(um| um)"

    if not (um_list := filter_all(condition, input_)):
        abort("Invalid IPv4 format.")
    
    print(um_list)