#!/usr/bin/env python3
"""Module measuring the runtime of four parallel async comprehensions."""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Run async_comprehension four times in parallel and time it.

    Returns:
        The total runtime in seconds, roughly ten because the four
        comprehensions run concurrently rather than one after another.
    """
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.perf_counter() - start
