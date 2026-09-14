"""Token-bucket rate limiter (single-node, thread-safe)."""
from __future__ import annotations

import threading
import time


class TokenBucket:
    def __init__(self, rate_per_sec: float, capacity: int) -> None:
        self.rate = rate_per_sec
        self.capacity = capacity
        self.tokens = float(capacity)
        self.updated = time.monotonic()
        self._lock = threading.Lock()

    def _refill(self) -> None:
        now = time.monotonic()
        self.tokens = min(self.capacity, self.tokens + (now - self.updated) * self.rate)
        self.updated = now

    def allow(self, cost: int = 1) -> bool:
        with self._lock:
            self._refill()
            if self.tokens >= cost:
                self.tokens -= cost
                return True
            return False


if __name__ == "__main__":
    bucket = TokenBucket(rate_per_sec=5, capacity=5)
    print([bucket.allow() for _ in range(7)])
