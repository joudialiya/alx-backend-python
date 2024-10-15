#!/usr/bin/env python3
"""Task module"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Task function"""
    start_timer = time.time()
    await asyncio.gather(*([async_comprehension()] * 4))
    return time.time() - start_timer
