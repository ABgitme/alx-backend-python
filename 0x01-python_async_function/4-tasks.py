#!/usr/bin/env python3
"""
This module defines an asynchronous coroutine that spawns `task_wait_random`
n times with a specified maximum delay and collects
the delays in ascending order.
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns `task_wait_random`
    n times with the specified max_delay.
    The delays are returned in ascending order
    without using the `sort()` function.

    Args:
        n (int): The number of times to spawn `task_wait_random`.
        max_delay (int): The maximum delay to be passed to `task_wait_random`.

    Returns:
        List[float]: List of all the delays in ascending order.

    Example:
        delays = await task_wait_n(5, 10)
        print(delays)  # Output: [0.34, 2.75, 3.91, 5.22, 9.01]
    """
    # Create and schedule the tasks using task_wait_random
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    # Use asyncio.gather to run all tasks concurrently and get their results
    delays = await asyncio.gather(*tasks)

    # Return delays in ascending order (we don't use sort)
    ordered_delays = []
    for delay in delays:
        i = 0
        while i < len(ordered_delays) and delay > ordered_delays[i]:
            i += 1
        ordered_delays.insert(i, delay)

    return ordered_delays
