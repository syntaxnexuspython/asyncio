# What is a Task?

# A Task is a wrapper around a coroutine.

# It tells the event loop:
# “Here’s some work to do — please schedule it and resume it whenever it can make progress.”

# When you call asyncio.create_task(coro()), you don’t just create a coroutine object — you tell the event loop to run it concurrently with other tasks.

# KEY PARTS OF TASK MANAGEMENT
import asyncio

async def worker(name, delay):
    print(f"{name} started")
    await asyncio.sleep(delay)
    print(f"{name} finished after {delay}s")

### Create Tasks

async def sub_main():
    # Create a Task
    task = asyncio.create_task(worker("A", 2.5)) # Returns a Task object.
    task2 = asyncio.create_task(worker("B", 1))
    task3 = asyncio.create_task(worker("C", 2))
    # Starts running immediately once the event loop cycles
    # Unlike just await worker(...) (which runs it directly), tasks run in the background
    # Checking Status
    print('is task done?', task.done())
    # Waiting for Tasks
    
    # Cancelling Tasks
    try:
        task3.cancel()
        await task3
    except asyncio.CancelledError:
        print('Task3 was cancelled')
    results = await asyncio.gather(task, task2) # Waiting for Tasks # You can await task to get its result

    # Task Groups

    async with asyncio.TaskGroup() as tg:
        for i in range(1, 11, 1):
            time_limit = i * 0.5
            tg.create_task(worker(f'Task {i}', time_limit))



# asyncio.run(sub_main())



async def fail():
    raise ValueError("Something went wrong")

async def work(x):
    await asyncio.sleep(1)
    return x * 2

async def gather_main():
    try:
        results = await asyncio.gather(fail(), work(2))
        print(results)
    except Exception as e:
        print("Caught:", e)



async def fail_group():
    raise ValueError("Something went wrong")

async def work_group(x):
    await asyncio.sleep(1)
    return x * 2

async def main_group():
    async with asyncio.TaskGroup() as tg:
        tg.create_task(work_group(1))
        tg.create_task(work_group(2))
        tg.create_task(fail_group())  # this fails

    # After the TaskGroup exits, all tasks are either completed or cancelled
    print("TaskGroup finished")

async def main():
    # await gather_main()
    await main_group()

asyncio.run(main())
