"""CRDTs: grow-only counter and last-writer-wins register."""
from dataclasses import dataclass, field


@dataclass
class GCounter:
    counts: dict[str, int] = field(default_factory=dict)

    def increment(self, node: str, delta: int = 1) -> None:
        self.counts[node] = self.counts.get(node, 0) + delta

    def value(self) -> int:
        return sum(self.counts.values())

    def merge(self, other: "GCounter") -> "GCounter":
        return GCounter({k: max(self.counts.get(k, 0), other.counts.get(k, 0))
                         for k in set(self.counts) | set(other.counts)})


@dataclass
class LwwRegister:
    value: object = None
    timestamp: int = -1

    def set(self, value: object, timestamp: int) -> None:
        if timestamp > self.timestamp:
            self.value, self.timestamp = value, timestamp

    def merge(self, other: "LwwRegister") -> "LwwRegister":
        return self if self.timestamp >= other.timestamp else other


if __name__ == "__main__":
    a, b = GCounter(), GCounter()
    a.increment("a", 3)
    b.increment("b", 2)
    assert a.merge(b).value() == 5

    register = LwwRegister()
    register.set("x", 1)
    register.set("y", 0)
    assert register.value == "x"
    print("crdt ok")
