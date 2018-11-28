"""
tee - using an output multiple times

As mentioned before, one of the biggest disadvantages of
generators is that the results are usable only once.
Luckily Python has a function that allows you to copy the
output to serveral generators.  The name `tee` might be familiar
to you if you are used to working in a command-line shell.
The `tee` program allows you to write outputs to both the screen
and a file, so you can store an output while still maintaining a live view
of it.

The Python version, `itertools.tee`, does a similar thing excecpt that it
returns several iterators, allowing you to process the results separately.

By default, `tee` will split your generator into a tuple containing two
different generators, which is why tuple unpacking works nicely here.  By
passing along the `n` paramter, this can easily be changed to support more than
2 generators.
"""

import itertools


def spam_and_eggs():
    yield 'spam'
    yield 'eggs'
    yield 'deer'
    yield 'xxx'


a, b, c, d, e = itertools.tee(spam_and_eggs(), 5)

print(next(a))
print(next(a))
print(next(a))
print(next(b))
print(next(b))
print(next(b))
print(next(c))
print(next(c))
print(next(c))
