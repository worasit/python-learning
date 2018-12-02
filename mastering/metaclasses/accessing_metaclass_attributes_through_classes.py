"""
When using metaclasses, ti might be confusing to note that the class actually does
more than simply construct the class, it acutally inherits the class during the
creation.  To inllustrate:
"""


class Meta(type):

    @property
    def spam(cls):
        return 'Spam property of %r' % cls

    def eggs(self):
        return 'Eggs method of %r' % self


class SomeClass(metaclass=Meta):
    pass


print(SomeClass.spam)
