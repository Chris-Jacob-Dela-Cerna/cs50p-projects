

import sys


def get_sys(idx, message="[Error  - System] Missing system argument."):
    try:
        sys_ = sys.argv[idx]
    except IndexError:
        sys.exit()
    return sys_