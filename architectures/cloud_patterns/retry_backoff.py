"""Retry with exponential backoff and jitter."""
from __future__ import annotations

import random
import time
from collections.abc import Callable
from typing import TypeVar

T = TypeVar("T")


def retry(
    fn: Callable[[], T],
    attempts: int = 5,
    base_delay: float = 0.1,
    max_delay: float = 5.0,
    retry_on: tuple[type[Exception], ...] = (Exception,),
) -> T:
    for attempt in range(1, attempts + 1):
        try:
            return fn()
        except retry_on:
            if attempt == attempts:
                raise
            delay = min(max_delay, base_delay * 2 ** (attempt - 1))
            delay += random.uniform(0, delay * 0.1)  # jitter
            time.sleep(delay)
    raise AssertionError("unreachable")


if __name__ == "__main__":
    calls = {"n": 0}

    def flaky() -> str:
        calls["n"] += 1
        if calls["n"] < 3:
            raise ConnectionError("temporary")
        return "ok"

    print(retry(flaky, base_delay=0.001))
