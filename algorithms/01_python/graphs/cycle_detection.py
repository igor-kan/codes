"""Cycle detection in directed (DFS colors) and undirected (DFS/DSU) graphs."""

from typing import List


def has_cycle_directed(n: int, adj: List[List[int]]) -> bool:
    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * n

    def dfs(u: int) -> bool:
        color[u] = GRAY
        for v in adj[u]:
            if color[v] == GRAY:
                return True
            if color[v] == WHITE and dfs(v):
                return True
        color[u] = BLACK
        return False

    for i in range(n):
        if color[i] == WHITE and dfs(i):
            return True
    return False


def has_cycle_undirected_dfs(n: int, edges: List[List[int]]) -> bool:
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    visited = [False] * n

    def dfs(u: int, parent: int) -> bool:
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                if dfs(v, u):
                    return True
            elif v != parent:
                return True
        return False

    for i in range(n):
        if not visited[i] and dfs(i, -1):
            return True
    return False


class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> bool:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        self.parent[rb] = ra
        return True


def has_cycle_undirected_dsu(n: int, edges: List[List[int]]) -> bool:
    dsu = DSU(n)
    for u, v in edges:
        if not dsu.union(u, v):
            return True
    return False


if __name__ == "__main__":
    assert has_cycle_directed(4, [[1], [2], [3], [1]])
    assert not has_cycle_directed(4, [[1], [2], [3], []])

    cycle_edges = [[0, 1], [1, 2], [2, 0]]
    tree_edges = [[0, 1], [1, 2], [1, 3]]
    assert has_cycle_undirected_dfs(4, cycle_edges)
    assert not has_cycle_undirected_dfs(4, tree_edges)
    assert has_cycle_undirected_dsu(3, cycle_edges)
    assert not has_cycle_undirected_dsu(4, tree_edges)
    print("[Python CycleDetection] Directed and undirected cycle detection verified.")
