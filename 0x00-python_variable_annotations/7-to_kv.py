#!/usr/bin/env python3
"""
This module provides utility functions
for manipulating key-value pairs, including
operations on strings and numerical values.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple where the first element
    is the string k, and the second element
    is the square of the numerical value v as a float.

    Args:
        k (str): A string key.
        v (Union[int, float]): A numerical value
        (either an integer or a float).

    Returns:
        Tuple[str, float]: A tuple with the string
        k and the square of v as a float.
    """
    return (k, float(v ** 2))
