import asyncio
import selectors

selector = selectors.SelectSelector()
event_loop = asyncio.SelectorEventLoop(selector)
asyncio.set_event_loop(event_loop)
