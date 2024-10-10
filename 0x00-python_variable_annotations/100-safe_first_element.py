#!/usr/bin/env python3
""" This a task module """
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Function to anotate"""
    if lst:
        return lst[0]
    else:
        return None
