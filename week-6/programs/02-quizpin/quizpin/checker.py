

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


def check_score(score, total):
    percentage = score / total * 100
    if percentage == 100:
        message = "A perfect score, bravo!"
    elif percentage >= 75:
        message = "What a great run!"
    elif percentage == 50:
        message = "Well done! Solid work."
    elif percentage >= 25:
        message = "You're getting there!"
    else:
        message = "A tough result, but a great learning opportunity."
    length = len(message) + 2
    outline = ""
    for _ in range(length):
        outline += "="
    return message, outline