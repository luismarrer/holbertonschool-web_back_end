#!/usr/bin/env python3
"""
Module 3-tasks

This module contains a function `task_wait_random` that creates an asyncio
Task from the `wait_random` coroutine.

Functions:
    task_wait_random(max_delay: int) -> asyncio.Task:
        Creates and returns an asyncio Task that will execute `wait_random`.
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio Task that will run the `wait_random` coroutine.

    Parameters:
    - max_delay (int): Maximum delay value for `wait_random`.

    Returns:
    - asyncio.Task: A Task object that can be awaited.
    """
    return asyncio.create_task(wait_random(max_delay))
