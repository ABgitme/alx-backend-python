#!/usr/bin/env python3

"""
This module provides a utility function for safely
retrieving a value from a dictionary
while handling missing keys by returning a default value.
"""

from typing import Any, Mapping, TypeVar, Union

T = TypeVar('T')


def safely_get_value(
        dct: Mapping, key: Any, default: Union[T, None] = None) ->\
        Union[Any, T]:
    """
    Safely retrieves a value from the dictionary using the provided key.
    If the key is not found, the function returns the default value.

    Args:
        dct (Mapping[Any, Any]): The dictionary from which
        to retrieve the value.
        key (Any): The key to search for in the dictionary.
        default (Union[T, None], optional): The default
        value to return if the key is not found. Defaults to None.

    Returns:
        Union[Any, T]: The value associated with the key,
        or the default value if the key is not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default
