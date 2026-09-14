"""Circuit Breaker: fail fast when a dependency is unhealthy."""
from __future__ import annotations

import time
from dataclasses import dataclass, field
from enum import Enum
from typing import Callable, TypeVar

T = TypeVar("T")


class State(Enum):
    CLOSED = "closed"
    OPEN = "open"
    HALF_OPEN = "half-open"


@dataclass
class CircuitBreaker:
    failure_threshold: int = 3
    reset_timeout: float = 5.0
    state: State = State.CLOSED
    failures: int = 0
    opened_at: float = 0.0

    def call(self, fn: Callable[[], T]) -> T:
        if self.state is State.OPEN:
            if time.monotonic() - self.opened_at >= self.reset_timeout:
                self.state = State.HALF_OPEN
            else:
                raise RuntimeError("circuit is open")
        try:
            result = fn()
        except Exception:
            self.failures += 1
            if self.failures >= self.failure_threshold:
                self.state = State.OPEN
                self.opened_at = time.monotonic()
            raise
        self.failures = 0
        self.state = State.CLOSED
        return result


if __name__ == "__main__":
    breaker = CircuitBreaker(failure_threshold=2)
    for _ in range(2):
        try:
            breaker.call(lambda: (_ for _ in ()).throw(ConnectionError("down")))
        except Exception as exc:  # noqa: BLE001
            print("caught", exc)
    print("state:", breaker.state.value)
