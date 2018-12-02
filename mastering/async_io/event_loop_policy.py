"""
Event loop policies

Event loop policies are objects that create and store the actual event loops for you.
They have been written with maximum flexibility in mind but are not objects that
you often need to modify.  The only reason I can think of modifying the event loop
policy is if you want to make specific event loops run on specific processors and/or
systems, or if you wish to change the default event loop type. Beyond that, it offers
more flexibility than most people will ever need.  Making your own event loop
(ProActorEventLoop in this case) the default is simply possible through this code
"""
import asyncio


class ProActorEventLoopPolicy(asyncio.events.BaseDefaultEventLoopPolicy):
    _loop_factory = asyncio.SelectorEventLoop


policy = ProActorEventLoopPolicy()
asyncio.set_event_loop(policy)
