#!/usr/bin/env python3
""" This a task module """
from functools import reduce
from typing import List


def sum_mixed_list(mxd_list: List[float | int]) -> float:
    """Reduce list"""
    return reduce(lambda e, p: e + p, mxd_list)
