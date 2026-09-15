"""A minimal SDN controller that installs forwarding rules."""
from dataclasses import dataclass, field
import heapq


@dataclass
class Switch:
    name: str
    ports: dict[str, str] = field(default_factory=dict)  # neighbor -> port
    flow_table: list[tuple[str, str]] = field(default_factory=list)  # (match, action)


class Controller:
    def __init__(self, topology: dict[str, dict[str, int]]) -> None:
        self.topology = topology
        self.switches: dict[str, Switch] = {node: Switch(node) for node in topology}

    def forwarding(self, source: str) -> dict[str, str]:
        dist = {node: float("inf") for node in self.topology}
        prev: dict[str, str | None] = {node: None for node in self.topology}
        dist[source] = 0
        heap = [(0, source)]
        while heap:
            d, node = heapq.heappop(heap)
            for neighbor, weight in self.topology[node].items():
                if d + weight < dist[neighbor]:
                    dist[neighbor] = d + weight
                    prev[neighbor] = node
                    heapq.heappush(heap, (dist[neighbor], neighbor))
        table: dict[str, str] = {}
        for node in prev:
            if node == source or prev[node] is None:
                continue
            hop = node
            while prev[hop] != source:
                hop = prev[hop]
            table[node] = hop
        return table

    def install(self, source: str) -> None:
        for node, next_hop in self.forwarding(source).items():
            self.switches[source].flow_table.append((f"dst={node}", f"out={next_hop}"))


if __name__ == "__main__":
    topology = {"s1": {"s2": 1, "s3": 2}, "s2": {"s1": 1, "s3": 1}, "s3": {"s1": 2, "s2": 1}}
    controller = Controller(topology)
    controller.install("s1")
    rules = dict(controller.switches["s1"].flow_table)
    assert rules["dst=s3"] == "out=s3" and rules["dst=s2"] == "out=s2"
    print("sdn controller ok")
