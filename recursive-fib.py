#!/usr/bin/python3

_cache = {
    0: 0,
    1: 1
}

def fibonacci(i):
    if i < 0:
        return None
    if i not in _cache:
        _cache[i] = fibonacci(i - 1) + fibonacci(i - 2)
    print(str(_cache))
    return _cache[i]
