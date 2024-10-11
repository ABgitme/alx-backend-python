#!/usr/bin/env python3
"""
This module provides utility functions for list operations,
including calculating
the length of each element in a list of sequences.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes an iterable of sequences (such as strings, lists, or tuples)
    and returns a list of tuples where each tuple
    contains the element and its length.

    Args:
        lst (Iterable[Sequence]): An iterable containing sequences
        (e.g., strings, lists, or tuples).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples
        where the first element is a sequence
        from the input iterable and the second
        element is its length.
    """
    return [(i, len(i)) for i in lst]
