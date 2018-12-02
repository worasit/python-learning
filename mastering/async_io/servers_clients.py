"""
One of the most common reason for stalling scripts and applications is the usage of
remote resources.  With `asyncio`, at least a large portion of that is easily fixable.
Fetching multiple remote resources and serving to multiple clients is quite a bit
easier amd more light weight than it used to be.  While both multithreading and
multiprocessing can be used for these cases as well, `asyncio` is a much lighter
alternative and it is actually easier to manage.  There are two main methods of creating
clients and servers.  The coroutine way is use
`asyncio.open_connection` and `sayncio.start_server`.  The class-based
approach requires you to inherit the `asyncio.Protocol` class. While these are
essentially the same thing, the workings are slightly different.

Basic echo server

The basic lient and server versions are simple enough to write.  The `asyncio`
module takes care of all the low-level connection handling, leaving us with only the
requirement of connecting the correct medhods. For the server, we need a method
to handle the incoming connections, and for the client, we need a function to create
connections. And to inllustrate what is happening and at which point in time, we will
add a dedicated print function that prints both the time since the server process
was started and the given arguments
"""

import time
import sys
import asyncio

HOST = '127.0.0.1'
PORT = 1234

start_time = time.time()


def printer(start_time, *args, **kwargs):
    '''Simple function to print a message prefixed with the
    time relative to the given start_time'''
    print('%.1f' % (time.time() - start_time), *args, **kwargs)


async def handle_connection(reader, writer):
    client_address = writer.get_extra_info('peername')
    printer(start_time, 'Client connected', client_address)

    # Send over the server start time to get consistent
    # timestamps
    writer.write(b'%.2f\n' % start_time)
    await writer.drain()

    repetitions = int((await reader.readline()))
    printer(start_time, 'Started sending to', client_address)

    for i in range(repetitions):
        message = 'client: %r, %d\n' % (client_address, i)
        printer(start_time, message, end='')
        writer.write(message.encode())
        await writer.drain()

    printer(start_time, 'Finished sending to', client_address)
    writer.close()


async def create_connection(repetitions):
    reader, writer = await asyncio.open_connection(
        host=HOST, port=PORT)

    start_time = float((await reader.readline()))

    writer.write(repetitions.encode() + b'\n')
    await writer.drain()

    async for line in reader:
        # Sleeping a little to emulate processing time and make
        # it easier to add more simultaneous clients
        await asyncio.sleep(1)

        printer(start_time, 'Got line: ', line.decode(),
                end='')

    writer.close()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    if sys.argv[1] == 'server':
        server = asyncio.start_server(
            handle_connection,
            host=HOST,
            port=PORT,
        )
        running_server = loop.run_until_complete(server)

        try:
            result = loop.call_later(5, loop.stop)
            loop.run_forever()
        except KeyboardInterrupt:
            pass

        running_server.close()
        loop.run_until_complete(running_server.wait_closed())
    elif sys.argv[1] == 'client':
        loop.run_until_complete(create_connection(sys.argv[2]))

    loop.close()
