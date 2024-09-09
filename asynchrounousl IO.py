import asyncio
from collections.abc import AsyncIterable
class AsyncRange(AsyncIterable):
    def __init__(self, start, end):
        self.start = start
        self.end = end
    async def __aiter__(self):
        for i in range(self.start, self.end):
            await asyncio.sleep(0.1)
            yield i

async def example():
    async for i in aiter(AsyncRange(1, 10)):
     print(i)
name = input("Provide your name: ")
     

asyncio.run(example())