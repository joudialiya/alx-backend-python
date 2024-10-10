#!/usr/bin/env python3
""" This a task module """
from functools import reduce


def sum_mixed_list(mxd_list: list[float | int]) -> float:
    """Reduce list"""
    return reduce(lambda e, p: e + p, mxd_list)
