#!/usr/bin/env python3
"""Helper computing the index range for a given pagination request."""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return the start and end indexes for the given page and page_size."""
    start = (page - 1) * page_size
    return (start, start + page_size)
