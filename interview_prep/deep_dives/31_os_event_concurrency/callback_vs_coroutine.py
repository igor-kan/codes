"""Callbacks vs coroutines yielding the same result."""
import asyncio


def schedule(callback, value) -> None:
    callback(value)  # synchronous stand-in for an event-loop dispatch


def callback_style(results: list[int]) -> None:
    def step(value: int) -> None:
        results.append(value + 10)

    schedule(step, 20)  # -> 30


async def coroutine_style() -> list[int]:
    async def compute() -> int:
        await asyncio.sleep(0)
        return 20

    value = await compute()
    return [value + 10]  # -> 30


if __name__ == "__main__":
    results: list[int] = []
    callback_style(results)
    assert results == [30]
    assert asyncio.run(coroutine_style()) == [30]
    print("callback and coroutine styles agree")
