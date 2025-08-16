# Asyncio
This is learning about asyncio and all it features

## Concurrent vs Parallel
### Concurrency
- Multiple tasks make progress during the same period of time
- Tasks may not literally run at the same instant, but they are interleaved — switching between tasks
- Example: A single person cooking:
    - Put rice on the stove (waiting to boil).
    - While waiting, chop vegetables.
    - While waiting for curry to simmer, set the table.
- Only one person is working, but many tasks are making progress concurrently.

### Parallelism
- Multiple tasks are executed at the exact same time on multiple processors/cores.
- Example: Two people cooking:
    - One cooks rice.
    - The other chops vegetables.
- They both run truly in parallel.

## Coroutine
- Coroutines are functions defined using the `async def` keyword. They can pause execution at certain points (await) and resume later, enabling non-blocking behavior
- Execution: Coroutines do not execute immediately when called. Instead, they return a coroutine object, which must be awaited or run using an event loop

## Event Loop
- It is responsible for managing and executing asynchronous tasks, callbacks, and I/O operations in a non-blocking manner
- It manages when and which coroutine runs.

- Instead of running everything at once, it switches between coroutines whenever they’re waiting (like on await asyncio.sleep(), I/O, network, etc.).

- It gives the illusion of doing many things at the same time (concurrency), it is doing things in concurrent nor parallel
