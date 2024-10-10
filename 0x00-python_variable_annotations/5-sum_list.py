#!/usr/bin/env python3
""" This a task module """
from functools import reduce
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Reduce list"""
    return reduce(lambda e, p: e + p, input_list)
