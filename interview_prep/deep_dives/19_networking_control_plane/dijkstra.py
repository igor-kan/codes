"""Link-state Dijkstra with predecessor tracking and forwarding table."""
import heapq


def dijkstra(adjacency: dict[str, dict[str, int]], source: str):
    dist = {node: float("inf") for node in adjacency}
    prev: dict[str, str | None] = {node: None for node in adjacency}
    dist[source] = 0
    visited: set[str] = set()
    heap = [(0, source)]
    while heap:
        d, node = heapq.heappop(heap)
        if node in visited:
            continue
        visited.add(node)
        for neighbor, weight in adjacency[node].items():
            if d + weight < dist[neighbor]:
                dist[neighbor] = d + weight
                prev[neighbor] = node
                heapq.heappush(heap, (dist[neighbor], neighbor))
    return dist, prev


def forwarding_table(prev: dict[str, str | None], source: str) -> dict[str, str]:
    table = {}
    for node in prev:
        if node == source:
            continue
        hop = node
        while prev[hop] and prev[hop] != source:
            hop = prev[hop]
        if prev[hop] == source:
            table[node] = hop
    return table


if __name__ == "__main__":
    graph = {
        "A": {"B": 2, "C": 5},
        "B": {"A": 2, "C": 1, "D": 4},
        "C": {"A": 5, "B": 1, "D": 1},
        "D": {"B": 4, "C": 1},
    }
    dist, prev = dijkstra(graph, "A")
    assert dist["D"] == 4 and dist["C"] == 3
    assert forwarding_table(prev, "A")["D"] == "B"
    print("dijkstra routing ok")
