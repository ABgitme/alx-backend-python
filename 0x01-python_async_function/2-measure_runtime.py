#!/usr/bin/env python3
"""
This module defines a function to measure
the average execution time
of the wait_n coroutine.
"""

import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay),
    and returns the average time per execution.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay to be passed to wait_random.

    Returns:
        float: The average time per execution.

    """
    start_time = time.time()  # Record the start time
    asyncio.run(wait_n(n, max_delay))  # Run the wait_n coroutine
    total_time = time.time() - start_time  # Calculate the total elapsed time

    return total_time / n  # Return the average time per execution
