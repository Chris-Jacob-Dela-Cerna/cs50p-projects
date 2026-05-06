

def checker(user, options):
    chosen = user.strip().lower()
    for item, option in options.items():
        if chosen == item:
            return option
    return None


def if_yes(user_select):
    chosen = user_select.strip().lower()
    if chosen == "y":
        return True
    return False