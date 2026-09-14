"""Async generators, queues and producers/consumers."""
import asyncio


async def producer(queue: asyncio.Queue, count: int) -> None:
    for i in range(count):
        await queue.put(i)
    await queue.put(None)


async def consumer(queue: asyncio.Queue, out: list) -> None:
    while (item := await queue.get()) is not None:
        out.append(item * item)


async def squares(count: int) -> list[int]:
    queue: asyncio.Queue = asyncio.Queue(maxsize=2)
    out: list[int] = []
    await asyncio.gather(producer(queue, count), consumer(queue, out))
    return out


async def main() -> None:
    assert await squares(5) == [0, 1, 4, 9, 16]


if __name__ == "__main__":
    asyncio.run(main())
    print("ok")
