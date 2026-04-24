# Document: This python is my 1st application of CS50P Week 5.

from calculator import n29


def test_addtion():
    assert n29.addition(3, 7) == 10

def test_subtraction():
    assert n29.subtraction(5, 3) == 2

def test_multiply():
    assert n29.multiply(3, 3) == 9

def test_divide():
    assert n29.divide(6, 3) == 9