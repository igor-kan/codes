"""Quorum reads/writes with R + W > N."""
from dataclasses import dataclass, field


@dataclass
class ReplicaSet:
    replicas: int
    values: list[tuple[int, int]] = field(default_factory=list)  # (version, value)

    def write(self, value: int, version: int, w: int) -> bool:
        if w > self.replicas:
            return False
        self.values = [(version, value)] * w
        return True

    def read(self, r: int, n: int) -> int | None:
        if r + n <= self.replicas:
            return None  # no overlap possible
        if not self.values:
            return None
        return max(self.values)[1]


if __name__ == "__main__":
    cluster = ReplicaSet(replicas=3)
    assert cluster.write(42, version=1, w=2)
    assert cluster.read(r=2, n=2) == 42
    assert cluster.read(r=1, n=1) is None
    print("quorum ok")
