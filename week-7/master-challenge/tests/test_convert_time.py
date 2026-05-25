

from src.convert_time import convert_hour
from src.convert_time import extract_time


def test_convert_hour():
    assert convert_hour("AM", 6) == 6
    assert convert_hour("AM", 12) == 0
    assert convert_hour("PM", 6) == 18
    assert convert_hour("PM", 12) == 24


def test_extract_time():
    assert extract_time("9:30") == (9, 30)
    assert extract_time("9") == (9, 0)