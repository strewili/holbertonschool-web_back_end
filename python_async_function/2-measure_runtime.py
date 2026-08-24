#!/usr/bin/env python3
"""Module measuring the average runtime of the wait_n coroutine."""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the average execution time of wait_n(n, max_delay).

    Args:
        n: how many coroutines wait_n spawns.
        max_delay: the upper bound passed to wait_n.

    Returns:
        The total execution time divided by n, as a float.
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start
    return total_time / n
