"""Edmonds-Karp maximum flow (BFS augmenting paths)."""
from collections import deque


def edmonds_karp(capacity: list[list[int]], source: int, sink: int) -> int:
    n = len(capacity)
    residual = [row[:] for row in capacity]
    flow = 0
    while True:
        parent = [-1] * n
        parent[source] = source
        queue = deque([source])
        while queue and parent[sink] == -1:
            u = queue.popleft()
            for v in range(n):
                if parent[v] == -1 and residual[u][v] > 0:
                    parent[v] = u
                    queue.append(v)
        if parent[sink] == -1:
            break
        path_flow = float("inf")
        v = sink
        while v != source:
            path_flow = min(path_flow, residual[parent[v]][v])
            v = parent[v]
        v = sink
        while v != source:
            u = parent[v]
            residual[u][v] -= path_flow
            residual[v][u] += path_flow
            v = u
        flow += path_flow
    return flow


if __name__ == "__main__":
    capacity = [
        [0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0],
    ]
    assert edmonds_karp(capacity, 0, 5) == 23
    print("edmonds-karp ok")
