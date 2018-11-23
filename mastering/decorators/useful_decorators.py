"""
The collection of the useful decorators

    - Single dispatch – polymorphism in Python (GenericType def sum[T](num1,num2))
    - ContextManager(with) statement made easy
    - Useless warning - how to ignore them
"""
import contextlib
import functools
import json
import pprint


@functools.singledispatch
def printer(value):
    print('other: %r' % value)


@printer.register(str)
def str_printer(value):
    print('str: %s' % value)


@printer.register(int)
def int_printer(value):
    print('int: %d' % value)


@printer.register(dict)
def dict_printer(value):
    print('dict:')
    for k, v in value.items():
        print('key: %r, value: %r' % (k, v))


printer('spam')
printer(123)
printer({1: 1, 2: 2})


# contextmanager or with statement
@contextlib.contextmanager
def open_context_manager(filename, mode='r'):
    fh = open(filename, mode)
    yield fh
    fh.close()


@contextlib.contextmanager
def debug(name):
    """
    The contextlib.contextmanager will wrap your function, and execute the function at 'yield'
    so you could modify the behavior of your function whatever you want
    :param name:
    """
    print('Debugging %r: ' % name)
    yield
    print('End of debugging %r' % name)


@debug('spam')
def spam():
    print('This is the inside of our spam function')


print(spam())
