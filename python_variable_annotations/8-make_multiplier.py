#!/usr/bin/env python3

"""
Module: make_multiplier

This module contains a function that generates a multiplier function.
The generated function multiplies a given float by a predefined multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a multiplier function that multiplies a
    given float by the specified multiplier.

    Parameters:
    multiplier (float): The number to multiply by.

    Returns:
    Callable[[float], float]: A function that takes a float
    as input and returns the result of multiplying it by the multiplier.

    Example Usage:
    >>> multiplier_3 = make_multiplier(3.0)
    >>> result = multiplier_3(10.0)
    >>> print(result)
    30.0

    >>> multiplier_2_5 = make_multiplier(2.5)
    >>> result = multiplier_2_5(4.0)
    >>> print(result)
    10.0
    """
    def multiplier_func(value: float) -> float:
        return value * multiplier
    return multiplier_func
