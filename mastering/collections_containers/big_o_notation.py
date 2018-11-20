"""
Time complexity – the big O notation
"""
import functools
import pprint
import timeit


def o_one(items):
    """
    The example of the O(1), execute only one time
    :return:
    :rtype:
    """
    return items[0]


def o_n(items):
    """
    The example of the O(n), execute n times
    :param items:
    :type items:
    :return:
    :rtype:
    """
    total = 0
    for _ in items:
        total = total + 1
    return total


def o_n_squared(items):
    """
    The example of the O(n**2), execute n*n times
    :param items:
    :type items:
    :return:
    :rtype:
    """
    total = 0
    for _ in items:
        for _ in items:
            total = total + 1
    return total


def __print(func, args=None):
    timer_ = timeit.Timer(functools.partial(func, args))
    pprint.pprint(f"{func.__name__}: {timer_.timeit(1)*10000000}")


ITEMS = range(1000)
__print(o_one, ITEMS)
__print(o_n, ITEMS)
__print(o_n_squared, ITEMS)

# ========= Result ===========
# 'o_one: 58.54999471921474'
# 'o_n: 639.5499985956121'
# 'o_n_squared: 693755.7800029026'
