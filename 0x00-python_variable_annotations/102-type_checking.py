#!/usr/bin/env python3
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zooms into an array by repeating each element
    according to the given factor.

    Args:
        lst (Tuple[int, ...]): A tuple of integers.
        factor (int, optional): The factor by which to zoom. Defaults to 2.

    Returns:
        List[int]: A list with elements repeated by the zoom factor.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)  # Defined as a tuple to match the function signature

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)  # Corrected the factor to an int
