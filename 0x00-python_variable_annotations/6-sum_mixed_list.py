#!/usr/bin/env python3
"""
This module provides utility functions
for operations on lists containing integers and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of all integers and floats in the input list.

    Args:
        mxd_lst (List[Union[int, float]]):
        A list of integers and floating point numbers.

    Returns:
        float: The sum of all the numbers in the list as a float.
    """
    return sum(mxd_lst)
