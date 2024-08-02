#!/usr/bin/env python3
"""returns a tuple as float"""


import typing


T = typing.TypeVar('T')


def safely_get_value(dct: typing.Mapping, key: typing.Any, default:
                     typing.Union[T, None] = None) -> \
        typing.Union[typing.Any, T]:
    """func of the function"""
    if key in dct:
        return dct[key]
    else:
        return default
