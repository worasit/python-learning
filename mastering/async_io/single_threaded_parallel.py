import asyncio


async def sleeper(delay):
    await asyncio.sleep(delay)
    print('Finished sleeper with delay: %d' % delay)


print('Start program')
loop = asyncio.get_event_loop()
tasks = (sleeper(1), sleeper(3), sleeper(2))
results = loop.run_until_complete(asyncio.wait(tasks))

print('End program')

# Finished sleeper with delay: 1
# Finished sleeper with delay: 2
# Finished sleeper with delay: 3
"""
Even though we stared the sleepers with the order of 1,3,2, which sleeps
for that amount of time, `asyncio.sleep` combined with the `await` statment
actually tells Python that it should just continue with a task that needs
actual processing at this time.  A regular `time.sleep` would actually stall
the Python task, meaning they would execute sequentially.  This make it somewhat 
more obviously transparent what these can be used for, as it handles any type of wait
which we can hand off to `ayncio` instead of keeping the entire Python thread bysy
"""
