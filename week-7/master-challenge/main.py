

import sys
from src.check_ip import check_ip
from src.convert_time import convert_time
from src.count_um import count_um
from src.extract_html import extract_html
from src.validate_email import validate_email


def main():
    try:
        mode = sys.argv[1]
    except IndexError:
        print("[Error  - System] No modes selected.")
        sys.exit(1)

    modes = {
        "ipv4": check_ip,
        "24hour": convert_time,
        "countum": count_um,
        "html": extract_html,
        "validate": validate_email,
    }

    if mode not in modes:
        sys.exit(1)
    modes[mode]()


if __name__ == "__main__":
    main()