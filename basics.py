import asyncio

# A co-routine
async def add(x: int, y: int):
  return x + y

# An event loop
loop = asyncio.get_event_loop()

# Pass the co-routine to the loop
result = loop.run_until_complete(add(3, 4))
print(result) # Prints 7