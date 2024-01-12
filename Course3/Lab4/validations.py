#!/usr/bin/env python3

def validate_user(username, minlen):
    if minlen < 1:
        raise ValueError("minlen must be at least 1")

    # Usernames can't be shorter than minlen
    if len(username) < minlen:
        return False

    # Usernames can only use letters, numbers, dots, and underscores
    if username[0].isalpha() and all(char.isalnum() or char in ('.', '_') for char in username):
        return True

    # Usernames can't begin with a number or other special characters
    else:
        return False

# Test cases
print(validate_user("blue.kale", 3))  # True
print(validate_user(".blue.kale", 3))  # False
print(validate_user("red_quinoa", 4))  # True
print(validate_user("_red_quinoa", 4))  # False

