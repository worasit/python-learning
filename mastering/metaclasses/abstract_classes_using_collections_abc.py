"""
The abstract base classes module is on of the most useful and most used examples
of metaclasses in Python, as it makes it easy to ensure that a class adheres to a
certain interface without a lot of manual checks.  We have already seen some
examples of abstract base classes in the previous chapters, but now we will look at
the inner workings of these and the more advanced features, sunc as custom ABSs.
"""
import abc


class Spam(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def some_method(self):
        raise NotImplemented()


class Eggs(Spam):
    def some_new_method(self):
        pass


# eggs = Eggs()
# Traceback (most recent call last):
#   File "/Users/worasitdaimongkol/Repositories/Python/python-learning/mastering/metaclasses/abstract_classes_using_collections_abc.py", line 23, in <module>
#     eggs = Eggs()
# TypeError: Can't instantiate abstract class Eggs with abstract methods some_method


class Bacon(Spam):

    def some_method(self):
        pass


bacon = Bacon()

'''
As you can see, the abstract base class blocks us form instantiating the classes until
all the abstract methods have been inherited.  In addition to the regular methods,
"property", "staticmethod", and "classmethod" are also supported
'''


class Animal(object, metaclass=abc.ABCMeta):

    @property
    @abc.abstractmethod
    def some_property(self):
        raise NotImplemented()

    @classmethod
    @abc.abstractmethod
    def some_classmethod(cls):
        raise NotImplemented()

    @staticmethod
    @abc.abstractmethod
    def some_staticmethod():
        raise NotImplemented()

    @abc.abstractmethod
    def some_instance_method(self):
        raise NotImplemented()
