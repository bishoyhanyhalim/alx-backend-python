#!/usr/bin/env python3
"""returns a tuple as float"""


import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """Returns a func by multiplier"""
    def float_multiply(x: float) -> float:
        return multiplier * x

    return float_multiply
