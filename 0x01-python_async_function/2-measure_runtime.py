#!/usr/bin/env python3
"""A Task module"""
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> int:
    """Task function"""
    start_clock = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time - start_clock) / n
