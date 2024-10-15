#!/usr/bin/env python3
"""Task module"""
import typing


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    """Task function"""
    return [n async for n in async_generator()]
