"""
Event loops:
    - async.SelectorEventLoop // More effient if performance is neccesary
    - async.ProactorEventLoop

import asyncio

event_loop = asyncio.ProactorEventLoop
asyncio.set_event_loop(event_loop)
"""

import sys
import selectors


def read(fh):
    print('Got input form stdin: %r' % fh.readline())


if __name__ == '__main__':
    # Create the defualt selector
    selector = selectors.DefaultSelector()

    # Register the read function for the READ event on stdin
    selector.register(sys.stdin, selectors.EVENT_READ, read)

    while True:
        for key, mask in selector.select():
            # The data attribute contains the read function here
            callback = key.data
            # Call it with the fileobj (stdin here)
            callback(key.fileobj)
