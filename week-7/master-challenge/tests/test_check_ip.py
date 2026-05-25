

from src.check_ip import check_ip_number


def test_check_ip_number():
    assert check_ip_number(["0", "0", "0", "256"]) == False
    assert check_ip_number(["0", "55", "155", "255"]) == True