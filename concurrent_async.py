import asyncio
import time


async def fetch_some_data():
    await asyncio.sleep(1)
    return "some data"

async def fetch_network_data():
    await asyncio.sleep(2)
    return "network data"

async def another_function():
    print("Another function started")
    await asyncio.sleep(3)
    print("Another function finished")
    return "another data"

async def normal_manual_function():
    start_time = time.time()

    some_data = asyncio.create_task(fetch_some_data())
    network_data = asyncio.create_task(fetch_network_data())
    another_func_data = asyncio.create_task(another_function())

    result_some_data = await some_data
    result_network_data = await network_data
    # result_another_data = await another_func_data

    print(result_some_data)
    print(result_network_data)
    # print(result_another_data)

    end_time = time.time()
    print("Total Time",end_time - start_time)


async def worker(name, delay):
    print(f"{name} started")
    await asyncio.sleep(delay)
    print(f"{name} finished after {delay}s")

async def main():
    tasks = [
        asyncio.create_task(normal_manual_function()),
        asyncio.create_task(worker("A", 2.5)),
        asyncio.create_task(worker("B", 1)),
        asyncio.create_task(worker("C", 2)),
    ]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())