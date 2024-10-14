#!/usr/bin/env python3
"""A Task module"""
import asyncio
import random


async def wait_random(max_delay: int) -> float:
    """Task function"""
    rand = random.uniform(0, max_delay)
    await asyncio.sleep(rand)
    return rand
