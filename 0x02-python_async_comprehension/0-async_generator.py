#!/usr/bin/env python3
"""Task module"""
import asyncio
import random
import typing


async def async_generator() -> typing.AsyncIterator[float]:
    """Task function"""
    for _ in range(0, 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
