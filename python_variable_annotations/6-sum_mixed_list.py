#!/usr/bin/env python3

"""
Module: 6-sum_mixed_list

This module contains a function to sum all the elements
in a list that can contain both integers and floating-point numbers.
"""

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    Sums all the elements in a list that can
    contain both integers and floating-point numbers.

    Parameters:
    mxd_list (List[Union[int, float]]): A list of integers
    and/or floating-point numbers to be summed.

    Returns:
    float: The sum of all the numbers in the list,
    returned as a floating-point number.

    Example Usage:
    >>> result = sum_mixed_list([1, 2.5, 3, 4.5])
    >>> print(result)
    11.0

    >>> result = sum_mixed_list([10, 20.5, 30, 40.5])
    >>> print(result)
    101.0
    """
    add = 0.0
    for num in mxd_list:
        add += num
    return add
