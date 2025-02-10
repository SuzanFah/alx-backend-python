#!/usr/bin/env python3
"""Module for concurrent coroutines"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with specified max_delay
    Args:
        n: number of times to spawn wait_random
        max_delay: maximum delay in seconds
    Returns:
        List of delays in ascending order
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
