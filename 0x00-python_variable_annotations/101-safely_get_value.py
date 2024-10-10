#!/usr/bin/env python3
""" This a task module """
from typing import Mapping, Any, TypeVar


T = TypeVar('T')


def safely_get_value(
        dct: Mapping,
        key: Any,
        default: T | None = None) -> T | Any:
    """Funtion to type annotate"""
    if key in dct:
        return dct[key]
    else:
        return default
