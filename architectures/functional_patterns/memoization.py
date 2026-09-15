"""Memoization with an LRU-bounded cache."""
from functools import lru_cache


@lru_cache(maxsize=128)
def fibonacci(n: int) -> int:
    return n if n < 2 else fibonacci(n - 1) + fibonacci(n - 2)


def memoize(fn):
    cache: dict = {}

    def wrapper(*args):
        if args not in cache:
            cache[args] = fn(*args)
        return cache[args]

    return wrapper


if __name__ == "__main__":
    assert fibonacci(50) == 12586269025

    @memoize
    def square(n: int) -> int:
        return n * n

    assert square(9) == 81 and square(9) == 81
    print("memoization ok")
