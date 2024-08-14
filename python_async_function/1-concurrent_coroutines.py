#!/usr/bin/env python3
"""
Module 1-concurrent_coroutines

This module contains an asynchronous function `wait_n` that spawns the
`wait_random` coroutine multiple times and returns a list of the delays
in ascending order.

Functions:
    wait_n(n: int, max_delay: int) -> List[float]:
        Spawns `wait_random` n times with the specified max_delay and returns
        the list of delays in ascending order.
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns `wait_random` n times with the specified max_delay.

    Parameters:
    - n (int): Number of times to spawn `wait_random`.
    - max_delay (int): Maximum delay value for `wait_random`.

    Returns:
    - List[float]: A list of delays in ascending order.
    """
    delays = []
    for _ in range(n):
        delay = await wait_random(max_delay)
        delays.append(delay)
    # Manually sort the delays in ascending order
    for i in range(len(delays)):
        for j in range(i + 1, len(delays)):
            if delays[i] > delays[j]:
                delays[i], delays[j] = delays[j], delays[i]
    return delays
