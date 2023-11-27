def add(a, b):
    if not isinstance(a, (int, float, complex)) or not isinstance(b, (int, float, complex)):
        raise ValueError("This is not a num!")
    else:
        return a + b
