#!/usr/bin/env python3
""" This a task module """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """return function annotation"""
    return lambda n: n * multiplier
