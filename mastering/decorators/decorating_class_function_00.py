"""
Decorating class function is very similar to the decorating function, but you need to be aware of the required first argument
'self' - the class instance.  You have most likely already used a few class function 'classmethod', 'staticmethod' and 'property'


Method:
    - Instance method (self)
    - Class method (cls)
    - Static method ()
"""

import pprint


class MoreSpam(object):
    def __init__(self, more=1):
        self.more = more

    def __get__(self, instance, cls):
        return self.more + instance.spam

    def __set__(self, instance, value):
        instance.spam = value - self.more


class Spam(object):
    more_spam = MoreSpam(5)

    def __init__(self, spam):
        self.registry = {}
        self.spam = spam

    def __getattr__(self, key):
        print('Getting %r' % key)
        return self.registry.get(key, 'Undefined')

    def __setattr__(self, key, value):
        if key == 'registry':
            object.__setattr__(self, key, value)
        else:
            print('Setting %r to %r' % (key, value))
            self.registry[key] = value

    def __delattr__(self, key):
        print('Deleting %r' % key)
        del self.registry[key]

    def some_instance_method(self, *args, **kwargs):
        print('self: %r' % self)
        print('args: %s' % pprint.pformat(args))
        print('kwargs: %s' % pprint.pformat(kwargs))

    # This case we need to be aware of the required first arg 'cls'
    @classmethod
    def some_class_method(cls, *args, **kwargs):
        print('cls: %r' % cls)
        print('args: %s' % pprint.pformat(args))
        print('kwargs: %s' % kwargs)

    # This case there is no first arg, because it is a static method
    @staticmethod
    def some_static_method(*args, **kwargs):
        print('name: %s' % Spam.some_static_method.__name__)
        print('args: %s' % pprint.pformat(args))
        print('kwargs: %s' % pprint.pformat(kwargs))


spam = Spam(1)

spam.some_instance_method(1, 2, a=3, b=4)
spam.some_class_method(1, 2, a=3, b=4)
Spam.some_static_method(1, 2, a=3, b=4)

print('spam.spam: %r' % spam.spam)
print('spam.more_spam: %r' % spam.more_spam)

print(spam.x)
spam.x = 8
print(spam.x)
del spam.x
print(spam.x)
