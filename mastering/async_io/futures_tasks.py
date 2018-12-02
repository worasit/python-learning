"""
Future and Tasks

The asyncio.Future class is essentially a promise of a result; it returs the
resutls if they are available, and once it receives results, it will pass them along to all
the registered callbacks.  It maintains a state vaiable internally, which allows an outside party
to mark a future as canceled.  The API is very similar to the `concurrent.futures.Future` class, but since they
are not fully compatiable, mask sure you do not confuse the two.

The `Future` class by itself is not that convenient to use though, so that is
where `asyncio.Task` comes in.  The `Task` class wraps a coroutine and automatically
handles the execution, results and state for you.  The coroytine will be executed
through the given event loop, or the defualt event loop if none was given.

The creation of these classes is not somethihng you need to worry about directly.
This is because instead of creating the class yourself, the recommended way is
through either `asyncio.ensure_future` or loop.create_task`.  The former
actually executes `loop.create_task` internally but it is more convenient if you
simply want to execute it on the main/default event loop without having to specify it
first.  The usage  is simple enough.  To create your own future manually, you simply
tell the event loop to execute `create_task` for you.  The following example is a
bit complicated because of all the setup code but the usage of C should be clear
enough.  The mos important aspect to note is that the event loop should be linked
so that the task knows how/where to run:
"""

import asyncio


async def sleeper(delay):
    await asyncio.sleep(delay)
    print('Finished sleeper with delay: %d' % delay)


# Create an event loop
event_loop = asyncio.get_event_loop()

# Create the task
result = event_loop.call_soon(event_loop.create_task, sleeper(1))

# Make sure the loop stops after 2 seconds
result = event_loop.call_later(2, event_loop.stop)

# Start the loop and make it run forever.  Or at least until the loop.stop gets
# called in 2 seconds
event_loop.run_forever()

print('End program')
