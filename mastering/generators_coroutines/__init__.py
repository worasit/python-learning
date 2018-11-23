"""
`A generator` is a specific type of iterator taht generates values through
a function.  While traditional methods build and return a `list` of
iterms, ad generator will simply `yield` every value separately at the
moment when they are requested by the caller.

    Pros:
    - Generators pause execution completely until the next value is
    yielded, which make them completely lazy.

    - Generators have no need to save values.  Whereas a traditional
    function would require creating a `list` and storing all results
    until they are returned, a generator only need to store a single
    value

    - Generators have infinite size.  There is no requirement to stop
    at a certain point

These preceding benefits come at a price, however.  The immediate results
of these benefits are a few disadvantage

    Cons:
    - Until you are done processing, you never know how many values are
    left; it could even be infinite.  This make usage dangerous in some
    cases; executing `list(some_infinite_generator)` will run out of
    memory

    - You cannot slice generators

    - You cannot get specific items without yielding all values before
    that index

    - You cannot restart a generator.  All values are yielded exactly one

 =================  Coroutines ===============

 Coroutiens are functions that allow for multitasking without requiring multiple threads
 or processes.  Whereas generators can only yield values from the caller while it is
 still running.  While this technique has a few limiations, if it suits your purpose,
 it can result in great performance at a very little cost.



The topics covered in this chapter are:
    - The characteristics and uses of generators
    - Generator comprehensions
    - Generator functions
    - Generator classes
    - Buldled generators
    - Coroutines
"""
