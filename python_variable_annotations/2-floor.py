#!/usr/bin/env python3

"""
Module: 2-floor

This module contains a simple function
to convert a floating-point number to
an integer by flooring it.
"""


def floor(n: float) -> int:
    """
    Converts a floating-point number to an integer by flooring it.

    Parameters:
    n (float): The floating-point number to be floored.

    Returns:
    int: The largest integer less than or equal to the given number.

    Example Usage:
    >>> result = floor(3.7)
    >>> print(result)
    3

    >>> result = floor(-2.3)
    >>> print(result)
    -2
    """
    return int(n)
