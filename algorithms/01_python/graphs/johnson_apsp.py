"""Johnson's algorithm: all-pairs shortest paths with negative edges."""
import heapq


def bellman_ford(n: int, edges: list[tuple[int, int, int]]) -> list[float] | None:
    dist = [0] * (n + 1)
    for _ in range(n):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            return None
    return dist


def johnson(n: int, edges: list[tuple[int, int, int]]) -> list[list[float]]:
    potential = bellman_ford(n, edges)
    if potential is None:
        raise ValueError("negative cycle")
    graph: dict[int, list[tuple[int, int]]] = {i: [] for i in range(n)}
    for u, v, w in edges:
        graph[u].append((v, w + potential[u] - potential[v]))
    result = []
    for source in range(n):
        dist = [float("inf")] * n
        dist[source] = 0
        heap = [(0, source)]
        while heap:
            d, node = heapq.heappop(heap)
            if d > dist[node]:
                continue
            for nxt, w in graph[node]:
                if d + w < dist[nxt]:
                    dist[nxt] = d + w
                    heapq.heappush(heap, (dist[nxt], nxt))
        result.append([dist[v] - potential[source] + potential[v] for v in range(n)])
    return result


if __name__ == "__main__":
    edges = [(0, 1, 3), (0, 2, 8), (1, 2, -2), (2, 3, 1), (1, 3, 5)]
    dist = johnson(4, edges)
    assert dist[0][2] == 1 and dist[0][3] == 2
    print("johnson apsp ok")
