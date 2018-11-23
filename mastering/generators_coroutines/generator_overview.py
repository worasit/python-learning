"""
A generator, in its simplest form, is a function that returns elements one at a time
instead of returning a collection of items.  The most important advantage of this is
that it requires very little memory and that it does not need to have predefined size.
"""

# Simple
import sys


def count(start=0, stop=sys.maxsize, step=1):
    n = start
    while n <= stop:
        yield n
        n += step


for i in count(1, 10):
    print(i)


# yield vs return
def generator():
    yield 'this is a generator'
    return 'this is return'


g = generator()
print(next(g))  # only display `this is a generator`
print(next(g))  # Traceback(err) - StopIteration: this is return
