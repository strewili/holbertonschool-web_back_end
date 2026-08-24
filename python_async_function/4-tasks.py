#!/usr/bin/env python3
"""Module spawning several wait_random tasks concurrently."""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn task_wait_random n times and return the delays in order.

    Args:
        n: how many tasks are spawned.
        max_delay: the upper bound passed to each task.

    Returns:
        The list of all delays, in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays: List[float] = []

    for completed in asyncio.as_completed(tasks):
        delays.append(await completed)

    return delays
