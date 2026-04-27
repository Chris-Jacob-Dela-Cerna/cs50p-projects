# Document: This python is my last application of CS50P Week 5.

from signup.n31 import convert_username


def test_convert_username():
    assert convert_username("  HexeusTGR528  ") == "HxsTGR528"