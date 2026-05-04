

def checker(user, modes):
    chosen = user.strip().lower()
    for letter, mode in modes.items():
        if chosen == letter:
            return mode
    return None