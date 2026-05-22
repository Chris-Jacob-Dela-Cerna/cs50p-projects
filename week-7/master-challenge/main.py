

import sys
from src.check_ip import check_ip
from src.convert_time import convert_time
from src.extract_html import extract_html


def main():
    try:
        mode = sys.argv[1]
    except IndexError:
        print("[Error  - System] No modes selected.")
        sys.exit(1)
    match mode:
        case "ipv4":
            check_ip()
        case "24hour":
            convert_time()
        case "countum":
            "count_um()"
        case "html":
            extract_html()
        case "validate()":
            "validate_email()"
        case _:
            print("[Error  - System] Invalid mode.")


if __name__ == "__main__":
    main()