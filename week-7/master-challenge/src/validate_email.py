

from utils.abort import abort
from validators import email


def validate_email():
    print("[Prompt - System] Enter email address:")
    input_ = input(">>> ").strip()

    if not email(input_):
        abort("Invalid email address.")
    
    print("[Success - System] Valid email address.")