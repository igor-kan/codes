"""Link-state routing with Dijkstra's shortest path."""
import heapq


def dijkstra(graph: dict[str, dict[str, int]], source: str) -> tuple[dict[str, int], dict[str, str | None]]:
    dist = {node: float("inf") for node in graph}
    prev: dict[str, str | None] = {node: None for node in graph}
    dist[source] = 0
    heap = [(0, source)]
    while heap:
        d, node = heapq.heappop(heap)
        if d > dist[node]:
            continue
        for neighbor, weight in graph[node].items():
            if d + weight < dist[neighbor]:
                dist[neighbor] = d + weight
                prev[neighbor] = node
                heapq.heappush(heap, (dist[neighbor], neighbor))
    return dist, prev


def path(prev: dict[str, str | None], target: str) -> list[str]:
    route = []
    while target is not None:
        route.append(target)
        target = prev[target]
    return route[::-1]


if __name__ == "__main__":
    graph = {
        "A": {"B": 1, "C": 4},
        "B": {"C": 2, "D": 5},
        "C": {"D": 1},
        "D": {},
    }
    dist, prev = dijkstra(graph, "A")
    assert dist["D"] == 4 and path(prev, "D") == ["A", "B", "C", "D"]
    print("route:", "->".join(path(prev, "D")))
