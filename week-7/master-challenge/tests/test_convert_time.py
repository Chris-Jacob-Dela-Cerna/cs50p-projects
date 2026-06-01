

from src.convert_time import convert_hour
from src.convert_time import extract_time
from utils.filter import filter_


def test_convert_hour():
    assert convert_hour("AM", 6) == 6
    assert convert_hour("AM", 12) == 0
    assert convert_hour("PM", 6) == 18
    assert convert_hour("PM", 12) == 24


def test_extract_time():
    assert extract_time("9:30") == (9, 30)
    assert extract_time("9") == (9, 0)
    

def test_filter_convert_time():
    condition = r"^([0-9]{1,2}(?::[0-9]{2})?) (AM|PM) to ([0-9]{1,2}(?::[0-9]{2})?) (AM|PM)$"
    assert filter_(condition, "9:30 to 5:30") == None
    assert filter_(condition, "9:30 AM - 5:30 PM") == None
    assert filter_(condition, "9 30 AM to 5 30 PM") == None
    assert filter_(condition, "9:30 am to 5:30 pm") == None
    assert filter_(condition, "9:30 AM to 5:30 PM").groups() == ("9:30", "AM", "5:30", "PM")