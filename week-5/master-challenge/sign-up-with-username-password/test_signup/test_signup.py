# Document: This python is my last application of CS50P Week 5.

from signup.signup import convert_username
from signup.signup import verify_username
from signup.signup import check_password
from signup.signup import verify_password


def test_convert_username_pass():
    assert convert_username("  HexeusTGR528  ") == "HxsTGR528"


def test_verify_username_pass():
    assert verify_username("HxsTGR528") == (True, "Username [HxsTGR528] saved successfully.")


def test_verify_username_fail():
    assert verify_username("Hx") == (False, "Invalid. There must be 3 or more characters.")
    assert verify_username("Hx 5") == (False, "Invalid. There must only be letters and numbers.")
    assert verify_username("Hx5") == (False, "Invalid. The first 3 characters should be letters.")
    assert verify_username("Hxs5TGR") == (False, "Invalid. After the 1st number, the rest should be numbers.")


def test_check_password_pass():
    dict0 = {
        "characters": 12,
        "letters": 6,
        "uppercase": 3,
        "lowercase": 3,
        "numbers": 3,
        "symbols": 3,
    }
    assert check_password("abcDEF123,./") == (True, dict0)


def test_check_password_fail():
    assert check_password("abcDEF12") == (False, "Invalid. There must be 9 or more characters.")
    assert check_password("abc 123,./") == (False, "Invalid. There must be no spaces.")


def test_verify_password_pass():
    dict0 = {
        "characters": 12,
        "letters": 6,
        "uppercase": 3,
        "lowercase": 3,
        "numbers": 3,
        "symbols": 3,
    }
    dict1 = {
        "characters": 11,
        "letters": 6,
        "uppercase": 3,
        "lowercase": 3,
        "numbers": 3,
        "symbols": 2,
    }
    dict2 = {
        "characters": 9,
        "letters": 6,
        "uppercase": 3,
        "lowercase": 3,
        "numbers": 3,
        "symbols": 0,
    }
    dict3 = {
        "characters": 10,
        "letters": 7,
        "uppercase": 1,
        "lowercase": 7,
        "numbers": 1,
        "symbols": 1,
    }
    assert verify_password(dict0) == (True, "Your password is very strong.")
    assert verify_password(dict1) == (True, "Your password is strong.")
    assert verify_password(dict2) == (True, "Your password is decent.")
    assert verify_password(dict3) == (False, "Your password is too weak.")