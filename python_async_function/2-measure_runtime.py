#!/usr/bin/env python3
"""
Module 2-measure_runtime

This module contains a function `measure_time` that measures the total
execution time for the function `wait_n` and returns the average time per
execution.

Functions:
    measure_time(n: int, max_delay: int) -> float:
        Measures the total execution time for
        `wait_n(n, max_delay)` and returns
        the average time per execution.
"""

import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for `wait_n(n, max_delay)` and returns
    the average time per execution.

    Parameters:
    - n (int): Number of times to spawn `wait_random`.
    - max_delay (int): Maximum delay value for `wait_random`.

    Returns:
    - float: The average time per execution.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
