"""asyncio tasks, gather and timeouts."""
import asyncio


async def fetch(name: str, delay: float) -> str:
    await asyncio.sleep(delay)
    return f"{name}:{delay}"


async def main() -> None:
    sequential = await fetch("a", 0.01)
    results = await asyncio.gather(fetch("b", 0.01), fetch("c", 0.01))
    assert sequential == "a:0.01"
    assert results == ["b:0.01", "c:0.01"]

    try:
        async with asyncio.timeout(0.01):
            await fetch("slow", 1)
    except TimeoutError:
        pass
    else:
        raise AssertionError("expected timeout")


if __name__ == "__main__":
    asyncio.run(main())
    print("ok")
