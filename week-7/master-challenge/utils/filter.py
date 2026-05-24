

import re


def filter_(condition, input_):
    if list_ := re.search(condition, input_):
        return list_
    return None


def filter_all(condition, input_):
    if list_ := re.findall(condition, input_):
        return list_
    return None