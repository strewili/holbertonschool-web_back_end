#!/usr/bin/env python3
"""Module that pairs each element of an iterable with its length."""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples pairing each element with its length.

    Args:
        lst: an iterable of sequences.

    Returns:
        A list of tuples, each containing an element of lst and its length.
    """
    return [(i, len(i)) for i in lst]
