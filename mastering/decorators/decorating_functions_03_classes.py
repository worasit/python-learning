"""
For the class, overide
    - __init__ : To prepare all required actions
    - __call__ : Implement your decorating logic here
"""

import functools


class Debug(object):
    def __init__(self, function):
        self.function = function
        self.output = None

    def __call__(self, *args, **kwargs):
        self.output = self.function(*args, **kwargs)
        self._print(args, kwargs)
        return self.output

    def _print(self, *args, **kwargs):
        print('%s(%r, %r): %r' %
              (self.function.__name__,
               args,
               kwargs,
               self.output))


@Debug
def spam(n):
    return 'spam' * n


spam(3)
