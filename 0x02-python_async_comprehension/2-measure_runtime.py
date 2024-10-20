#!/usr/bin/env python3
"""measuring time"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total runtime of executing
    async_comprehension four times in parallel.

    This coroutine runs four instances of
    async_comprehension concurrently
    using asyncio.gather and returns the total runtime.

    Returns:
        float: The total runtime in seconds.
    """
    start_time = time.perf_counter()  # Record the start time

    # Execute async_comprehension four times in parallel
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())

    end_time = time.perf_counter()  # Record the end time
    return end_time - start_time  # Calculate and return the total runtime
