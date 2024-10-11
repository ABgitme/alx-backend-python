#!/usr/bin/env python3
"""
This module provides utility functions
for creating customized multiplier functions
that multiply a given float by a predefined factor.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a multiplier function that
    multiplies a float by the given multiplier.

    Args:
        multiplier (float): The factor by which to
        multiply floats.

    Returns:
        Callable[[float], float]: A function that
        takes a float and returns the product of
        that float and the multiplier.
    """
    def multiplier_function(value: float) -> float:
        return value * multiplier

    return multiplier_function
