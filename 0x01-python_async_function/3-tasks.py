#!/usr/bin/env python3
"""
This module defines a function
that creates an asyncio.Task
from the wait_random coroutine.
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio.
    Task that schedules the wait_random coroutine.

    Args:
        max_delay (int): The maximum delay to be passed to wait_random.

    Returns:
        asyncio.Task: The task object that schedules wait_random.

    Example:
        task = task_wait_random(5)
        print(task)  # Output: <Task pending name='Task-1'>
    """
    return asyncio.create_task(wait_random(max_delay))
