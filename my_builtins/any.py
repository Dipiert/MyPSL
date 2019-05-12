def any(iterable):
    """Return True if any element of the iterable is true.
    If the iterable is empty, return False.
    """
    for i in iterable:
        if i:
            return True
    return False
