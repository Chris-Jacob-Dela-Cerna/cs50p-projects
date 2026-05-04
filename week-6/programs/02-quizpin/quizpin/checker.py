

def checker(user, options):
    chosen = user.strip().lower()
    for item, option in options.items():
        if chosen == item:
            return option
    return None