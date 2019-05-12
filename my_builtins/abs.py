
def abs(x):
    """Return the absolute value of a number.
       The argument may be an integer or a floating point number.
       If the argument is a complex number, its magnitude is returned.
    """
    if not isinstance(x, (int, float, complex)):
        raise TypeError(f"bad operand type for abs(): '{type(x).__name__}'")
    return x if x >= 0 else x * -1
