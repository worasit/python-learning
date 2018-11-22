"""
 Debugging/Logging examples
"""

import functools


def debug(function):
    @functools.wraps(function)
    def _debug(*args, **kwargs):
        output = function(*args, **kwargs)
        print('%s(%r, %r): %r' % (function.__name__, args, kwargs, output))
        return output

    return _debug


@debug
def spam(eggs):
    return 'spam' * (eggs % 5)


spam(3)
