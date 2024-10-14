#!/usr/bin/env python3
"""
This module defines an asynchronous coroutine that spawns
`wait_random` n times with a specified maximum delay,
collecting the delays in an ascending order.
"""

from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns `wait_random`
    n times with the specified max_delay.
    The delays are returned in ascending order without
    using the `sort()` function.

    Args:
        n (int): The number of times to spawn `wait_random`.
        max_delay (int): The maximum delay to be passed to `wait_random`.

    Returns:
        list[float]: List of all the delays in ascending order.

    Example:
        delays = await wait_n(5, 10)
        print(delays)  # Output: [0.34, 2.75, 3.91, 5.22, 9.01]
    """
    delays = []
    for _ in range(n):
        delay = await wait_random(max_delay)
        # Insert the delay in ascending order
        # by placing it in the correct position
        i = 0
        while i < len(delays) and delay > delays[i]:
            i += 1
        delays.insert(i, delay)

    return delays
