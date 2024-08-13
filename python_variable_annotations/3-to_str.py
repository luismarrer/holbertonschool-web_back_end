#!/usr/bin/env python3

"""
Module: 3-to_str

This module contains a simple function
to convert a floating-point number to a string.
"""


def to_str(n: float) -> str:
    """
    Converts a floating-point number to a string.

    Parameters:
    n (float): The floating-point number to be converted.

    Returns:
    str: The string representation of the given number.

    Example Usage:
    >>> result = to_str(3.14)
    >>> print(result)
    '3.14'

    >>> result = to_str(42.0)
    >>> print(result)
    '42.0'
    """
    return str(n)
