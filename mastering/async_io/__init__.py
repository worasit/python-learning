"""
    Function using
        - async def
        - async for
        - async with
        - await
    Parallel execution
    Servers
    Clients
    Eventual result using `Future`


Concepts of asyncio

The `asyncio` libray has sevaral basic concepts, which have to
be explained before we venture further into examples and uses.
The example shown in the previous paragraph actually used mos of them,
but a little explaination about the how an the why might stell be useful.

The amin concepts of `asyncio` are `Coroutines` and `Event loops`.  Within them,
there are several helper classes available, such as `Steams`, `Futures`, and `Processes`
The next few paragraphs will explain the basics so that you can understand the implementation in
the examples in the later paragraphs
"""

import asyncio


# old version
@asyncio.coroutine
def async_old_version():
    yield from asyncio.sleep(1)


# new version(the suggested one)
async def async_new_version():
    """
    The interpreter checks whether the object is an
    awaitable object, meaning it needs to be one of
    the following
        - A native coroutine created with the `async def` statement
        - A coroutine created with the `asyncio.coroutine` decorator
        - An object that implements the `__await__` method
    """
    await asyncio.sleep(1)
