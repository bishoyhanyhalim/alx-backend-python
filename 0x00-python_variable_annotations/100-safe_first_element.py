#!/usr/bin/env python3
"""returns a tuple as float"""


import typing


def safe_first_element(lst: typing.Sequence[typing.Any]) -> \
        typing.Union[typing.Any, None]:
    """func for annotation"""
    if lst:
        return lst[0]
    else:
        return None
