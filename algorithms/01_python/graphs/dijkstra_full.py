import heapq
from typing import Dict, List, Tuple, Optional


class Graph:
    def __init__(self):
        self.adj: Dict[int, List[Tuple[int, float]]] = {}

    def add_edge(self, u: int, v: int, weight: float, bidirectional: bool = True):
        self.adj.setdefault(u, []).append((v, weight))
        self.adj.setdefault(v, [])
        if bidirectional:
            self.adj[v].append((u, weight))

    def dijkstra(self, source: int) -> Tuple[Dict[int, float], Dict[int, Optional[int]]]:
        dist: Dict[int, float] = {node: float("inf") for node in self.adj}
        parent: Dict[int, Optional[int]] = {node: None for node in self.adj}
        dist[source] = 0.0

        pq: List[Tuple[float, int]] = [(0.0, source)]

        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue

            for v, weight in self.adj[u]:
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    parent[v] = u
                    heapq.heappush(pq, (dist[v], v))

        return dist, parent


if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1, 4.0)
    g.add_edge(0, 2, 1.0)
    g.add_edge(2, 1, 2.0)
    g.add_edge(1, 3, 1.0)
    g.add_edge(2, 3, 5.0)

    dist, parent = g.dijkstra(0)
    assert dist[3] == 4.0
    print("[Python Dijkstra] Shortest paths computed successfully.")
