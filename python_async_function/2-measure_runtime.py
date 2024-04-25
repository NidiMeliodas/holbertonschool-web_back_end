#!/usr/bin/env python3
"""
function with integers n and max_delay as arguments
that measures the total execution time for wait_n(n, max_delay),
and returns total_time / n.
Your function should return a float.
"""
import asyncio
import time

wait_random = __import__('0-basic_async_syntax').wait_random
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    function should return a float.
    """
    begin_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    return (end_time - begin_time) / n
