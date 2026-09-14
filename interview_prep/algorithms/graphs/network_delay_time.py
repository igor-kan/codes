import heapq


def network_delay(times: list[list[int]], n: int, k: int) -> int:
    graph: dict[int, list[tuple[int, int]]] = {}
    for src, dst, weight in times:
        graph.setdefault(src, []).append((dst, weight))
    dist = {i: float("inf") for i in range(1, n + 1)}
    dist[k] = 0
    heap = [(0, k)]
    while heap:
        d, node = heapq.heappop(heap)
        if d > dist[node]:
            continue
        for nxt, weight in graph.get(node, []):
            if d + weight < dist[nxt]:
                dist[nxt] = d + weight
                heapq.heappush(heap, (dist[nxt], nxt))
    longest = max(dist.values())
    return -1 if longest == float("inf") else int(longest)


if __name__ == "__main__":
    assert network_delay([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2) == 2
    print("ok")
