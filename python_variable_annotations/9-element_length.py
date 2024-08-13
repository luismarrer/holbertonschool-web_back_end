#!/usr/bin/env python3

"""
Module: 9-element_length

This module contains a function that takes an iterable of
sequences and returns a list of tuples.
Each tuple contains a sequence from the iterable and its corresponding length.
"""

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Computes the length of each sequence in an iterable.

    Parameters:
    lst (Iterable[Sequence]): An iterable
    containing sequences (e.g., strings, lists, tuples).

    Returns:
    List[Tuple[Sequence, int]]: A list of tuples,
    where each tuple contains a sequence from the iterable and its length.

    Example Usage:
    >>> result = element_length(["apple", "banana", "cherry"])
    >>> print(result)
    [('apple', 5), ('banana', 6), ('cherry', 6)]

    >>> result = element_length([(1, 2), (3, 4, 5), [6]])
    >>> print(result)
    [((1, 2), 2), ((3, 4, 5), 3), ([6], 1)]
    """
    return [(i, len(i)) for i in lst]
