#!/usr/bin/env python3

"""
Module: 5-sum_list

This module contains a function to sum all
the elements in a list of floating-point numbers.
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Sums all the elements in a list of floating-point numbers.

    Parameters:
    input_list (list[float]): A list of floating-point numbers to be summed.

    Returns:
    float: The sum of all the numbers in the list.

    Example Usage:
    >>> result = sum_list([1.2, 2.3, 3.4])
    >>> print(result)
    6.9

    >>> result = sum_list([0.5, 1.5, 2.5, 3.5])
    >>> print(result)
    8.0
    """
    result = 0
    for num in input_list:
        result = result + num
    return result
