#!/usr/bin/env python3
"""
This module defines an asynchronous generator
function that yields random numbers
between 0 and 10 with a delay of 1 second between each yield.
"""
import asyncio
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronously generates 10 random numbers between 0 and 10.

    This coroutine loops 10 times,
    waiting for 1 second asynchronously on each iteration,
    then yields a random floating-point number in the range [0, 10).

    Yields:
        float: A random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)  # yield a random float between 0 and 10
