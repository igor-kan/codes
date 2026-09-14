"""Kahn's algorithm: indegree-based topological sort with cycle detection."""

from collections import deque
from typing import List, Optional


def kahn_topological_sort(n: int, edges: List[List[int]]) -> Optional[List[int]]:
    adj = [[] for _ in range(n)]
    indegree = [0] * n
    for u, v in edges:
        adj[u].append(v)
        indegree[v] += 1

    queue = deque([i for i in range(n) if indegree[i] == 0])
    order = []
    while queue:
        u = queue.popleft()
        order.append(u)
        for v in adj[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)

    if len(order) != n:
        return None
    return order


if __name__ == "__main__":
    edges = [[5, 2], [5, 0], [4, 0], [4, 1], [2, 3], [3, 1]]
    order = kahn_topological_sort(6, edges)
    assert order is not None
    pos = {node: i for i, node in enumerate(order)}
    for u, v in edges:
        assert pos[u] < pos[v]
    assert kahn_topological_sort(3, [[0, 1], [1, 2], [2, 0]]) is None
    print(f"[Python Kahn] Topological order: {order}")
