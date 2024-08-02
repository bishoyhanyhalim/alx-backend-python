#!/usr/bin/env python3
"""returns a tuple as float"""


import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """returns a tuple as float"""
    return (k, float(v * v))
