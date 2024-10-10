#!/usr/bin/env python3
""" This a task module """
from functools import reduce
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Reduce list"""
    return reduce(lambda e, p: e + p, mxd_list)
