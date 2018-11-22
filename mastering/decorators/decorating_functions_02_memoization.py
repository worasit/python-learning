"""
Memoization is a way of caching the results of a function call.  If a function is memoized,
the evaluating it is simply a matter of looking up the result you got the first time the function was called
with those parameters

For the example below, we do the calculation of Fibonacci, let say that
if we calculate for fibonacci(1000) in classic version, we need to re-calculate the value
from 1 to n again, which is very bad for time complexity(BigO)

Eventually, we do not need to implement the @memoize ourself, since the Python
has introduced the 'lry_cache' which is similar to the preceding memorize function
"""
import functools


def memoize(_function):
    _function.cache = dict()

    @functools.wraps(_function)
    def _memoize(*args):
        if args not in _function.cache:
            _function.cache[args] = _function(*args)
        return _function.cache[args]

    return _memoize


@memoize
def classic_fibonacci(n):
    if n < 2:
        return n
    return classic_fibonacci(n - 1) + classic_fibonacci(n - 2)


for i in range(1, 10):
    print('fibonacci %d: %d' % (i, classic_fibonacci(i)))

print(classic_fibonacci.__wrapped__.cache)


# ============= lru_cache (least recently used cache) =========
def counter(function):
    function.calls = 0

    @functools.wraps(function)
    def _counter(*args, **kwargs):
        function.calls += 1
        return function(*args, **kwargs)

    return _counter


@functools.lru_cache(maxsize=3)
@counter
def lru_fibonacci(n):
    if n < 2:
        return n
    return lru_fibonacci(n - 1) + lru_fibonacci(n - 2)


print(lru_fibonacci(100))
print(lru_fibonacci.cache_info())
print(lru_fibonacci.__wrapped__.__wrapped__.calls)
