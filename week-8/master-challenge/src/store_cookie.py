

import sys
from data.cookie_jar import Jar
from utils.get_sys import get_sys


def store_cookie():
    capacity = get_sys(2, "Please enter the cookie jar's capacity.")
    try:
        jar = Jar(capacity)
    except ValueError as ve:
        sys.exit("[Error  - System] " + str(ve))