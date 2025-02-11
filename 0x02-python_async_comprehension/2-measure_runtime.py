#!/usr/bin/env python3
"""Module for measuring runtime of parallel async comprehensions"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension 4 times in parallel and measures total runtime
    Returns:
        Total runtime in seconds
    """
    start_time = time.perf_counter()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    return time.perf_counter() - start_time
