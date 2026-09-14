"""Load balancing strategies: round-robin, weighted, least-connections."""
from __future__ import annotations

import itertools
import random
from dataclasses import dataclass, field


@dataclass
class Backend:
    name: str
    weight: int = 1
    connections: int = 0


class RoundRobin:
    def __init__(self, backends: list[Backend]) -> None:
        self._cycle = itertools.cycle(backends)

    def pick(self) -> Backend:
        return next(self._cycle)


class WeightedRandom:
    def __init__(self, backends: list[Backend]) -> None:
        self.backends = backends

    def pick(self) -> Backend:
        return random.choices(
            self.backends, weights=[b.weight for b in self.backends], k=1
        )[0]


class LeastConnections:
    def __init__(self, backends: list[Backend]) -> None:
        self.backends = backends

    def pick(self) -> Backend:
        return min(self.backends, key=lambda b: b.connections)


if __name__ == "__main__":
    pool = [Backend("a", weight=2), Backend("b"), Backend("c")]
    rr = RoundRobin(pool)
    print([rr.pick().name for _ in range(6)])
