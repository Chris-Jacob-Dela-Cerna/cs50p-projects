

import sys


def main():
    try:
        mode = sys.argv[1]
    except IndexError:
        print("[Error  - System] No modes selected.")
        sys.exit()
    match mode:
        case "ipv4":
            "check_ip()"
        case "html":
            "extract_html()"
        case "24hour":
            "convert_time()"
        case "validate()":
            "validate_email()"


if __name__ == "__main__":
    main()