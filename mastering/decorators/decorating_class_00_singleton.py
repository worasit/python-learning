"""
Class decorators are not different with the regular one,
except the fact that they take a class instead of a function

The class decorator occasionally uses in the real world, since
we have an alternative way such as 'inheritance'

Use cases:
    - Singletons – classes with a single instance
    - Total ordering – sortable classes the easy way
"""

import functools


def singleton(cls):
    instances = dict()

    @functools.wraps(cls)
    def _singleton(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return _singleton


@singleton
class Spam(object):
    def __init__(self):
        print('Executing init')


spam_a = Spam()
spam_b = Spam()

print('spam_a is spam_b: %r' % (spam_a is spam_b))

spam_a.xx = 123

print('spam_a.xx: %r' % spam_a.xx)
print('spam_b.xx: %r' % spam_b.xx)
