"""
Return True if any element of the iterable is true.
If the iterable is empty, return False. Equivalent to:
"""
def any(iterable):
    for i in iterable:
        if i:
            return True
    return False
