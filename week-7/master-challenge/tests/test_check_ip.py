

from src.check_ip import check_ip_number
from utils.filter import filter_


def test_check_ip_number():
    assert check_ip_number(["0", "0", "0", "256"]) == False
    assert check_ip_number(["0", "0", "0", "0"]) == True
    assert check_ip_number(["0", "55", "155", "255"]) == True


def test_filter_check_ip():
    condition = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"
    assert filter_(condition, "0 0 0 0") == None
    assert filter_(condition, "0.0.0") == None
    assert filter_(condition, "0.0.0.0.0") == None
    assert filter_(condition, "0.0.0.-1") == None
    assert filter_(condition, "0.0.0.0").groups() == ("0", "0", "0", "0")
    assert filter_(condition, "0.55.155.255").groups() == ("0", "55", "155", "255")