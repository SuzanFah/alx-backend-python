#!/usr/bin/env python3
"""Module for creating asyncio Tasks"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio.Task for wait_random
    Args:
        max_delay: maximum delay in seconds
    Returns:
        asyncio.Task object
    """
    return asyncio.create_task(wait_random(max_delay))
