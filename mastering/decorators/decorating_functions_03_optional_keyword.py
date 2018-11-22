import functools


def add(*args, **kwargs):
    'Add n to the input of the decorated function'

    # The default kwargs, we don't store this in kwargs
    # because we want to make sure that args and kwargs
    # can't both be filled
    default_kwargs = dict(n=1)

    # The inner function, notice that this is actually a
    # decorator itself
    def _add(function):
        # The actual function that will be called
        @functools.wraps(function)
        def __add(n):
            default_kwargs.update(kwargs)
            return function(n + default_kwargs['n'])

        return __add

    if len(args) == 1 and callable(args[0]) and not kwargs:
        # Decorator call without arguments, just call it
        # ourselves
        return _add(args[0])
    elif not args and kwargs:
        # Decorator call with arguments, this time it will
        # automatically be executed with function as the
        # first argument
        default_kwargs.update(kwargs)
        return _add
    else:
        raise RuntimeError('This decorator only supports '
                           'keyword arguments')


@add
def spam(n):
    return 'spam' * n


@add(n=3)
def eggs(n):
    return 'eggs' * n


spam(3)

eggs(2)


@add(3)
def bacon(n):
    return 'bacon' * n
