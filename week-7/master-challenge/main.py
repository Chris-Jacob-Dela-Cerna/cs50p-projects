

import sys
from src.check_ip import check_ip


def main():
    try:
        mode = sys.argv[1]
    except IndexError:
        print("[Error  - System] No modes selected.")
        sys.exit(1)
    match mode:
        case "ipv4":
            check_ip()
        case "html":
            "extract_html()"
        case "24hour":
            "convert_time()"
        case "validate()":
            "validate_email()"
        case _:
            print("[Error  - System] Invalid mode.")


if __name__ == "__main__":
    main()