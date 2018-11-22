"""
Decorators with (optional) arguments
"""

import functools


def add(extra_n):
    def _add(function):
        @functools.wraps(function)
        def __add(n):
            return function(n + extra_n)

        return __add

    return _add


@add(extra_n=1)
def eggs(n):
    return 'eggs' * n


print(eggs(1))
# result
# eggseggs


print(add(eggs)(2))
