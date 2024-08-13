#!/usr/bin/env python3

"""
Module: 1-concat

This module contains a simple function to concatenate two strings.
"""


def concat(str1: str, str2: str) -> str:
    """
    Concatenates two strings.

    Parameters:
    str1 (str): The first string to concatenate.
    str2 (str): The second string to concatenate.

    Returns:
    str: The concatenation of the two strings.

    Example Usage:
    >>> result = concat("Hello, ", "world!")
    >>> print(result)
    Hello, world!
    """
    return str1 + str2
