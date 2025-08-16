import asyncio


async def async_function() -> None:
    print("hello from before sleep")
    await asyncio.sleep(2)
    print("hello from after sleep")


async def main() -> None:
    print("Before starting function")
    await asyncio.sleep(1)

    await async_function()

    await asyncio.sleep(1)

    print("After finishing function")


if __name__ == "__main__":
    asyncio.run(main())
