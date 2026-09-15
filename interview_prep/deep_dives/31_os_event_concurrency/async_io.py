"""asyncio with tasks, queues and graceful cancellation."""
import asyncio


async def worker(name: str, queue: asyncio.Queue, results: list) -> None:
    while True:
        item = await queue.get()
        if item is None:
            queue.task_done()
            break
        results.append(f"{name}:{item}")
        queue.task_done()


async def main() -> list[str]:
    queue: asyncio.Queue = asyncio.Queue()
    results: list[str] = []
    workers = [asyncio.create_task(worker(f"w{i}", queue, results)) for i in range(3)]
    for i in range(9):
        await queue.put(i)
    await queue.join()
    for _ in workers:
        await queue.put(None)
    await asyncio.gather(*workers)
    return results


if __name__ == "__main__":
    results = asyncio.run(main())
    assert len(results) == 9
    print("async io ok:", sorted(results)[:3], "...")
