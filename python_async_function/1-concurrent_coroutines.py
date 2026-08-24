#!/usr/bin/env python3
"""Module spawning several wait_random coroutines concurrently."""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times and return the delays in ascending order.

    Args:
        n: how many times wait_random is spawned.
        max_delay: the upper bound passed to each wait_random call.

    Returns:
        The list of all delays, sorted in ascending order without using
        sort(), thanks to the order in which the coroutines complete.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays: List[float] = []

    for completed in asyncio.as_completed(tasks):
        delays.append(await completed)

    return delays
