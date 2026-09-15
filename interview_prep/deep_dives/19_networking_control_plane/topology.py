"""Represent and analyse a network topology graph."""
from dataclasses import dataclass, field


@dataclass
class Topology:
    adjacency: dict[str, dict[str, int]] = field(default_factory=dict)

    def add_link(self, a: str, b: str, cost: int) -> None:
        self.adjacency.setdefault(a, {})[b] = cost
        self.adjacency.setdefault(b, {})[a] = cost

    def degree(self, node: str) -> int:
        return len(self.adjacency.get(node, {}))

    def is_connected(self) -> bool:
        if not self.adjacency:
            return True
        start = next(iter(self.adjacency))
        seen = {start}
        stack = [start]
        while stack:
            node = stack.pop()
            for neighbor in self.adjacency[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append(neighbor)
        return len(seen) == len(self.adjacency)


if __name__ == "__main__":
    topo = Topology()
    topo.add_link("A", "B", 1)
    topo.add_link("B", "C", 2)
    assert topo.is_connected() and topo.degree("B") == 2
    topo.add_link("D", "E", 1)
    assert not topo.is_connected()
    print("topology ok")
