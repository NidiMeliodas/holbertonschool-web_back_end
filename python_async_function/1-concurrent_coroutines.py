#!/usr/bin/env python3
"""
write an async routine called wait_n that takes in 2 int arguments
(in this order): n and max_delay. You will spawn wait_random n times
with the specified max_delay.
wait_n should return the list of all the delays (float values). The
list of the delays should be in ascending order without using sort()
because of concurrency.
"""
import asyncio
from typing import List

wait_rdm = __import__('0-basic_async_syntax').wait_rdm


async def wait_n(n: int, max_delay: int) -> List[float]:
    """async routine called wait_n that takes in 2 int arguments"""
    task = [wait_rdm(max_delay) for i in range(n)]
    delay = await asyncio.gather(*task)
    return sorted(delay)
