"""Throttling: fixed-window rate limit per key."""
import time


class FixedWindowThrottle:
    def __init__(self, limit: int, window_s: float, clock=time.monotonic) -> None:
        self.limit = limit
        self.window_s = window_s
        self.clock = clock
        self.counts: dict[tuple[str, int], int] = {}

    def allow(self, key: str) -> bool:
        window = int(self.clock() / self.window_s)
        bucket = (key, window)
        self.counts[bucket] = self.counts.get(bucket, 0) + 1
        return self.counts[bucket] <= self.limit


if __name__ == "__main__":
    throttle = FixedWindowThrottle(2, 1000)
    assert throttle.allow("u1") and throttle.allow("u1")
    assert not throttle.allow("u1")
    print("throttling ok")
