#!/usr/bin/env python3
"""
This module provides a function to return
the floor value of a floating-point number.
"""

import math


def floor(n: float) -> int:
    """
    Returns the floor of the given floating-point number.

    Args:
        n (float): The floating-point number to floor.

    Returns:
        int: The largest integer less than or equal to the given float.
    """
    return math.floor(n)
