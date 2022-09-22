#!/usr/bin/python3

"""
Modules add_integer define function
to do add operation and handle Type
Error
"""

def add_integer(a, b=98):
    """ add to integer or float
    Args:
    a (int): first number
    b (int): second number (optional)
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)


