#!/usr/bin/python3

from functools import reduce

def greatest_common_divisor(a, b):
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)

def _lowest_common_multiple(a, b):
    return a * b // greatest_common_divisor(a, b)

def lowest_common_multiple(*args):
    return reduce(_lowest_common_multiple, args)
