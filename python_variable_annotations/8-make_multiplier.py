#!/usr/bin/env python3
"""Module that creates multiplier functions."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by multiplier.

    Args:
        multiplier: the float used to multiply the future argument.

    Returns:
        A function taking a float and returning that float multiplied by
        multiplier.
    """
    def multiplier_function(value: float) -> float:
        """Multiply the given float by the captured multiplier."""
        return value * multiplier

    return multiplier_function
