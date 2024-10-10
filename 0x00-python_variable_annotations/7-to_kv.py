#!/usr/bin/env python3
""" This a task module """
from functools import reduce
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, int | float]:
    """tuple annotation"""
    return (k, v ** 2)
