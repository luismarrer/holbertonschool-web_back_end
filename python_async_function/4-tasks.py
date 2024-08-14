#!/usr/bin/env python3
"""
Module 4-tasks

This module contains a function `task_wait_n` that spawns multiple asyncio
Tasks using the `task_wait_random` function and returns a list of the delays
in ascending order.

Functions:
    task_wait_n(n: int, max_delay: int) -> List[float]:
        Spawns `task_wait_random` n times with
        the specified max_delay and returns
        the list of delays in ascending order.
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns `task_wait_random` n times with the specified max_delay.

    Parameters:
    - n (int): Number of times to spawn `task_wait_random`.
    - max_delay (int): Maximum delay value for `task_wait_random`.

    Returns:
    - List[float]: A list of delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    for i in range(len(delays)):
        for j in range(i + 1, len(delays)):
            if delays[i] > delays[j]:
                delays[i], delays[j] = delays[j], delays[i]
    return delays
