#!/usr/bin/env python3
"""Module wrapping the wait_random coroutine into an asyncio Task."""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Create an asyncio Task running wait_random(max_delay).

    Args:
        max_delay: the upper bound passed to wait_random.

    Returns:
        The asyncio.Task wrapping the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
