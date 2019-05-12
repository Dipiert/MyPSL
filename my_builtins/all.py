def all(iterable):
    """Return True if all elements of the iterable are true (or if the iterable is empty)."""
    for i in iterable:
        if not i:
            return False
    return True
