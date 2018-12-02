"""
Metaclasses are the factories that create new clesases in Python.  In fact, even
though you may not be aware of it, Python willalways execute the `type`
metaclass whenever you create a class.

When creating classes in a procedura way, the `type` metaclass is used as a
function.  This function takes three arguments: "name", "bases", and "dict".
The name will become the "__name__" arttibute, the "bases" is the list of inherited
base classes and will be stored in "__bases__" and "dict" is the name space
dictionary that contains all variables and will be stored in "__dict__"

It should be noted that the "type()" function has another use as well.  Given the
argments docuemented earlier, it creates a class given thoses specifications.  Given a
single argument with the instance of a class, it will return the class as well but from
the instance.  Your next question might be, "What happens if I call "type()" on a
class definition instead of ca class instance?" Well, that returns the metaclass for the
class which is "type" by default
"""


# Normal class creation
class Spam(object):
    eggs = 'my eggs'


print('Normal version of class creation')
spam = Spam()
print(spam.eggs)
print(type(spam))

print('Special version of class creation using "type() function"')
spam = type('Spam', (object,), dict(eggs='my eggs'))
print(spam.eggs)
print(type(spam))

'''
As expected the results for the two are the same.  When creating a class, Python
silently asdds the 'type' metaclass and 'custom' metaclasses are simply classes
that inherit 'type'.  A simple class definition has a silent metaclass making a simple
definition such as:

class Spam(object):
    pass
    
Essentially identical to:

class Spam(object, metaclass=type)
    pass
    
This raises the question that if every class is created by a (silent) metaclass, what is
the metaclass of 'type'?  This is actually a recursive definition; the metaclass of
'type' is 'type'.  This is the essence of what a custom metaclass is: a class that
inherits type to allow class modification without needing to modify the class definition itself.
'''
