#!/usr/bin/env python3
""" This a task module """
from typing import Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> list[tuple[Sequence, int]]:
    """Function to anotate"""
    return [(i, len(i)) for i in lst]
