#!/usr/bin/env python3
""" This a task module """
from functools import reduce


def sum_list(input_list: list[float]) -> float:
    """Reduce list"""
    return reduce(lambda e, p: e + p, input_list)
