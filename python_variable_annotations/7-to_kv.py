#!/usr/bin/env python3

"""
Module: to_kv

This module contains a function that takes a string and
a number (integer or float) and returns a tuple.
The tuple contains the string and the square of the number as a float.
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Creates a tuple with a string and the square of a given number.

    Parameters:
    k (str): The string to include in the tuple.
    v (Union[int, float]): The number to square and include in the tuple.

    Returns:
    Tuple[str, float]: A tuple where the first element is the string
    `k` and the second element is the square of `v`, returned as a float.

    Example Usage:
    >>> result = to_kv("age", 5)
    >>> print(result)
    ('age', 25.0)

    >>> result = to_kv("height", 2.5)
    >>> print(result)
    ('height', 6.25)
    """
    tup: Tuple[str, float] = (k, v**2)
    return tup
