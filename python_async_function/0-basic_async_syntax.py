#!/usr/bin/env python3
"""
Module 0-basic_async_syntax

This module contains an asynchronous function `wait_random` that waits
for a random delay between 0 and `max_delay` seconds and returns the delay.

The `wait_random` function is useful in scenarios where you need to introduce
a random delay, such as simulating network latency or adding randomness
to a process.

Functions:
    wait_random(max_delay: int = 10) -> float:
        Asynchronously waits for a random delay between 0
        and `max_delay` seconds
        and returns the actual delay.

Example:
    >>> import asyncio
    >>> from 0-basic_async_syntax import wait_random
    >>> delay = asyncio.run(wait_random(5))
    >>> print(f"Waited for {delay} seconds.")
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random
    delay between 0 and max_delay seconds
    and returns the delay.

    Parameters:
    - max_delay (int): The maximum delay in seconds. Default is 10.

    Returns:
    - float: The actual delay in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
