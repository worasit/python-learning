"""
To be defined

Use cases:
    - Debugging
        - printing input/output

"""
import functools


def eggs(function):
    """
    To make the syntax esiser to use, Python has a special syntax for this case.
    So, instead of adding a line such as the following example

    spam = eggs(spam)

    you can simply decorate a function using the @functools.wraps

    @eggs
    def spam():
        pass

    The decorator simply receives the function and returns a function

    Note: without functiontools.wraps it will lose the function context
        - __doc__
        - __name__
        - __module__
        - __annotations__
        - __qualname__
    :param function:
    :type function:
    :return:
    :rtype:
    """

    @functools.wraps(function)
    def _eggs(*args, **kwargs):
        print('%r got args: %r and kwargs: %r' % (
            function.__name__, args, kwargs
        ))
        return function(*args, **kwargs)

    return _eggs


@eggs
def spam(a, b, c):
    """The spam function return a * b + c"""
    return a * b + c


spam(1, 2, 3)
help(spam)
print(spam.__name__)
