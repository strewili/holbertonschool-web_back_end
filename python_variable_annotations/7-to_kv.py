#!/usr/bin/env python3
"""Module that builds a key/value tuple from a string and a number."""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple holding a string and the square of a number.

    Args:
        k: the string used as the first element of the tuple.
        v: the integer or float that gets squared.

    Returns:
        A tuple whose first element is k and whose second element is the
        square of v as a float.
    """
    return (k, float(v ** 2))
