#!/usr/bin/env python3
"""Module for measuring execution time"""

import time
import asyncio
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures total execution time for wait_n(n, max_delay)
    Args:
        n: number of times to spawn wait_random
        max_delay: maximum delay in seconds
    Returns:
        Average time per operation (total_time / n)
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.perf_counter() - start_time
    return total_time / n
