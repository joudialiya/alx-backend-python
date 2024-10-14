#!/usr/bin/env python3
"""A Task module"""
import typing
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """Task function"""
    ret = await asyncio.gather(*[wait_random(max_delay) for _ in range(0, n)])
    # sorting
    for i in range(0, len(ret)):
        for j in range(i, len(ret)):
            if ret[i] > ret[j]:
                ret[i], ret[j] = ret[j], ret[i]
    return ret
