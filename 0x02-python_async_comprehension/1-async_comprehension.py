#!/usr/bin/env python3
"""Generates a list from an async comprehension"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers asynchronously
    from async_generator using async comprehension.

    This coroutine asynchronously collects the 10
    values yielded by async_generator
    and returns them as a list.

    Returns:
        List[float]: A list of 10 random numbers generated
        by async_generator.
    """
    return [number async for number in async_generator()]
