#!/usr/bin/env python3
"""Module that sums a list of floats."""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Return the sum of a list of floats.

    Args:
        input_list: a list containing floats.

    Returns:
        The sum of every element of input_list as a float.
    """
    return sum(input_list)
