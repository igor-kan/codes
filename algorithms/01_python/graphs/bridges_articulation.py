"""Tarjan's algorithm for bridges and articulation points in an undirected graph."""

from typing import List, Set, Tuple


def find_bridges(n: int, edges: List[List[int]]) -> Set[Tuple[int, int]]:
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    disc = [-1] * n
    low = [-1] * n
    bridges = set()
    timer = 0

    def dfs(u: int, parent: int):
        nonlocal timer
        disc[u] = low[u] = timer
        timer += 1
        for v in adj[u]:
            if v == parent:
                continue
            if disc[v] == -1:
                dfs(v, u)
                low[u] = min(low[u], low[v])
                if low[v] > disc[u]:
                    bridges.add((min(u, v), max(u, v)))
            else:
                low[u] = min(low[u], disc[v])

    for i in range(n):
        if disc[i] == -1:
            dfs(i, -1)
    return bridges


def find_articulation_points(n: int, edges: List[List[int]]) -> Set[int]:
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    disc = [-1] * n
    low = [-1] * n
    ap = set()
    timer = 0

    def dfs(u: int, parent: int):
        nonlocal timer
        disc[u] = low[u] = timer
        timer += 1
        children = 0
        for v in adj[u]:
            if v == parent:
                continue
            if disc[v] == -1:
                children += 1
                dfs(v, u)
                low[u] = min(low[u], low[v])
                if parent != -1 and low[v] >= disc[u]:
                    ap.add(u)
            else:
                low[u] = min(low[u], disc[v])
        if parent == -1 and children > 1:
            ap.add(u)

    for i in range(n):
        if disc[i] == -1:
            dfs(i, -1)
    return ap


if __name__ == "__main__":
    edges = [[0, 1], [1, 2], [2, 0], [1, 3]]
    bridges = find_bridges(4, edges)
    assert bridges == {(1, 3)}, bridges
    aps = find_articulation_points(4, edges)
    assert aps == {1}, aps

    edges2 = [[0, 1], [1, 2], [2, 3]]
    assert find_bridges(4, edges2) == {(0, 1), (1, 2), (2, 3)}
    assert find_articulation_points(4, edges2) == {1, 2}
    print("[Python BridgesArticulation] Tarjan's algorithm verified.")
