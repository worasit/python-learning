"""
Arguments to metaclasses

The possibility of adding arguments to  a metaclass is a little-known feature, but
very useful nonetheless.  In many cases, simply adding attributes or methods to a
class definition is enough to detect what to do, but there are cases where it is useful
to be more specific.
"""


class MetaWithArguments(type):
    def __init__(metaclass, name, bases, namespace, **kwargs):
        return type.__init__(metaclass, name, bases, namespace)

    def __new__(metaclass, name, bases, namespace, **kwargs):
        for k, v in kwargs.items():
            namespace.setdefault(k, v)

        return type.__new__(metaclass, name, bases, namespace)


class WithArguement(metaclass=MetaWithArguments, spam='eggs'):
    pass


with_argument = WithArguement()
print(with_argument.spam)

'''
This simplistic example may not be useful but the possibilities are.  The only thing
you need to keep in mind is that both the '__name__' and '__init__' methods
need to be extended for this to work.
'''
