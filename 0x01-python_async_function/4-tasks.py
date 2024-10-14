#!/usr/bin/env python3
"""A Task module"""
import typing
import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    """Task function"""
    futures = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*futures)
    return delays
