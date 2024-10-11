#!/usr/bin/env python3
"""
This module provides utility functions
for safely handling list operations, including
retrieving the first element of a list while
handling empty lists gracefully.
"""

from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Safely returns the first element of
    a sequence (e.g., list, string, tuple).
    If the sequence is empty, it returns None.

    Args:
        lst (Sequence[Any]): A sequence of elements
        (the types of the elements are not known).

    Returns:
        Union[Any, None]: The first element of the
        sequence if it exists, otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
