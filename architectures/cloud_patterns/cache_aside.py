"""Cache-Aside: load on miss, write through to the store."""
from __future__ import annotations

from collections.abc import Callable
from typing import TypeVar

T = TypeVar("T")


class CacheAside:
    def __init__(self, loader: Callable[[str], T], ttl_seconds: int = 60) -> None:
        self._loader = loader
        self._ttl = ttl_seconds
        self._cache: dict[str, tuple[T, float]] = {}
        self.hits = 0
        self.misses = 0

    def get(self, key: str) -> T:
        import time

        now = time.monotonic()
        if (entry := self._cache.get(key)) and entry[1] > now:
            self.hits += 1
            return entry[0]
        self.misses += 1
        value = self._loader(key)
        self._cache[key] = (value, now + self._ttl)
        return value

    def invalidate(self, key: str) -> None:
        self._cache.pop(key, None)


if __name__ == "__main__":
    store = {"a": 1, "b": 2}
    cache = CacheAside(store.__getitem__)
    print(cache.get("a"), cache.get("a"), cache.get("b"))
    print("hits", cache.hits, "misses", cache.misses)
