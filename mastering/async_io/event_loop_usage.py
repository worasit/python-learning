"""
Event loop:
    - call_soon :
        Add an item to the end of the (FIFO)queqe so that
        the function will be executed in the order in which
        they were interested.
    - call_soon_treadsafe:
        This is the same as 'call_soon' except for being
         thread safe.  The 'call_soon' method is not thread
         safe because thread safety requires the usage of the
         global interpreter lock(GIL), which effectively makes
         your program single threaded at the moment of thread safety.
         The performance chapter will explain more thoroughly
    - call_later:
        Call the function after the given number of seconds.  If two
        jobs would runat the same time, they will run in an undefined
        order.  Note that the delay is a minimum.  If the event loop is
        locked/bysy, it can run later.
    - call_at:
        Call a function at a specific time related to the output of
        `loop.time`.  Every integer after `loop.time` adds a seconds

All of these functions return `asyncio.Handle` objects.  These objects
allow the cancellation of the task through the `handle.cancel`
"""

import time
import asyncio

start = time.time()


def printer(name):
    print('Started %s at %.1f' % (name, time.time() - start))
    time.sleep(0.2)
    print('Finished %s at %.1f' % (name, time.time() - start))


event_loop = asyncio.get_event_loop()
result = event_loop.call_at(event_loop.time() + .2, printer, 'call_at')
result = event_loop.call_later(.1, printer, 'call_later')
result = event_loop.call_soon(printer, 'call_soon')
result = event_loop.call_soon_threadsafe(printer, 'call_soon_threadsafe')

# Make sure we stop after a second
result = event_loop.call_later(1, event_loop.stop)

event_loop.run_forever()
