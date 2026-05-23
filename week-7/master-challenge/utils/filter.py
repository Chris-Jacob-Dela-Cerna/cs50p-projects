

import re


def filter_(condition, input_):
    if group := re.search(condition, input_):
        return group
    return None