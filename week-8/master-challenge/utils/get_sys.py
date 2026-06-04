

import sys


def get_sys(idx, message=" Missing system argument."):
    try:
        sys_ = sys.argv[idx]
    except IndexError:
        sys.exit("[Error  - System] " + message)
    return sys_