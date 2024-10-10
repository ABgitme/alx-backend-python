"""
This module provides utility functions for operations on lists of floats.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of all floats in the input list.
    Args:
        input_list (List[float]): A list of floating point numbers.
    Returns:
        float: The sum of all the floats in the list.
    """
    return sum(input_list)
