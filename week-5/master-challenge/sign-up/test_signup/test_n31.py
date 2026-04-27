# Document: This python is my last application of CS50P Week 5.

from signup.n31 import convert_username
from signup.n31 import verify_username


def test_convert_username_if_pass():
    assert convert_username("  HexeusTGR528  ") == "HxsTGR528"

def test_verify_username_if_pass():
    assert verify_username("HxsTGR528") == (True, "Username [HxsTGR528] saved successfully.")

def test_verify_username_if_fail():
    assert verify_username("Hx") == (False, "Invalid. There must be 3 or more characters.")
    assert verify_username("Hx 5") == (False, "Invalid. There must only be letters and numbers.")
    assert verify_username("Hx5") == (False, "Invalid. The first 3 characters should be letters.")
    assert verify_username("Hxs5TGR") == (False, "Invalid. After the 1st number, the rest should be numbers.")