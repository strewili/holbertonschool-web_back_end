#!/usr/bin/env python3
"""Module providing an asynchronous coroutine that waits a random delay."""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random delay and return it.

    Args:
        max_delay: the upper bound of the random delay, in seconds.

    Returns:
        The random delay that was waited, as a float.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
