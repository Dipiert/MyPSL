def abs(x):
    if not isinstance(x, (int, float, complex)):
        raise TypeError(f"bad operand type for abs(): '{type(x).__name__}'")
    return x if x >= 0 else x * -1
