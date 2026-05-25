

from src.convert_time import extract_time


def test_extract_time():
    assert extract_time("9:30") == (9, 30)
    assert extract_time("9") == (9, 0)