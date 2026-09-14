"""Hierholzer's algorithm for Eulerian path/circuit in an undirected graph."""

from typing import List, Dict, Optional


def find_eulerian_path(n: int, edges: List[List[int]]) -> Optional[List[int]]:
    adj: Dict[int, List[List[int]]] = {i: [] for i in range(n)}
    for idx, (u, v) in enumerate(edges):
        adj[u].append([v, idx])
        adj[v].append([u, idx])

    odd = [v for v in range(n) if len(adj[v]) % 2 == 1]
    if len(odd) not in (0, 2):
        return None
    start = odd[0] if odd else 0

    stack = [start]
    path = []
    while stack:
        u = stack[-1]
        while adj[u]:
            v, idx = adj[u].pop()
            # Remove the reverse edge from v's adjacency list
            adj[v] = [e for e in adj[v] if e[1] != idx]
            u = v
            stack.append(u)
        path.append(stack.pop())
    return path[::-1]


if __name__ == "__main__":
    # Eulerian circuit on a triangle
    circuit = find_eulerian_path(3, [[0, 1], [1, 2], [2, 0]])
    assert circuit is not None and len(circuit) == 4, circuit
    assert circuit[0] == circuit[-1]

    # Eulerian path on two triangles sharing a vertex: odd-degree nodes exist
    edges = [[0, 1], [1, 2], [2, 0], [0, 3], [3, 4], [4, 0]]
    path = find_eulerian_path(5, edges)
    assert path is not None and len(path) == len(edges) + 1, path

    # No Eulerian path (4 odd-degree nodes)
    assert find_eulerian_path(4, [[0, 1], [0, 2], [0, 3]]) is None
    print("[Python EulerianPath] Hierholzer's algorithm verified.")
