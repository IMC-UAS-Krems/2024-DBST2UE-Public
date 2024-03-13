def sum(a, b):
    """ A simple, but broken, addition function"""

    if a == 0:
        # Pretend this is an error. We'll expose this by testing
        return a - b
    else:
        return a + b