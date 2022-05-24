Parallelism consists of performing multiple operations at the same time. Multiprocessing is a means to effect parallelism, and it entails spreading tasks over a computer’s central processing units (CPUs, or cores). Multiprocessing is well-suited for CPU-bound tasks: tightly bound for loops and mathematical computations usually fall into this category.

Concurrency is a slightly broader term than parallelism. It suggests that multiple tasks have the ability to run in an overlapping manner. (There’s a saying that concurrency does not imply parallelism.)

Threading is a concurrent execution model whereby multiple threads take turns executing tasks. One process can contain multiple threads. Python has a complicated relationship with threading thanks to its GIL, but that’s beyond the scope of this article.

EVENT LOOP
In order to use Asyncio, we will need an event loop, a way input tasks to be done in this loop
Event loops run asynchronous tasks and callbacks, perform network IO operations, and run subprocesses


**Coroutine vs futures**
A coroutine is a generator function that can both yield values and accept values from the outside. The benefit of using a coroutine is that we can pause the execution of a function and resume it later. In case of a network operation, it makes sense to pause the execution of a function while we're waiting for the response. We can use the time to run some other functions.

A future is like the Promise objects from Javascript. It is like a placeholder for a value that will be materialized in the future. In the above-mentioned case, while waiting on network I/O, a function can give us a container, a promise that it will fill the container with the value when the operation completes. We hold on to the future object and when it's fulfilled, we can call a method on it to retrieve the actual result.

A function is all-or-nothing. Once it starts, it won’t stop until it hits a return, then pushes that value to the caller (the function that calls it). A generator, on the other hand, pauses each time it hits a yield and goes no further. Not only can it push this value to calling stack, but it can keep a hold of its local variables when you resume it by calling next() on it.

**Co-routine vs Task in asyncio**
Python asyncio provides two basic constructs for running on the event loop.
1.Co-routine
2.Asyncio task

Co-routines are created using async def syntax

There are two ways to make an asyncio task:
# 1
loop = asyncio.get_event_loop()
loop.create_task(cor) 

# 2
import asyncio
asyncio.create_task(cor)