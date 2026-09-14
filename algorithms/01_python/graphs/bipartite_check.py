"""Bipartite graph check via BFS/DFS two-coloring."""

from collections import deque
from typing import List


def is_bipartite_bfs(n: int, adj: List[List[int]]) -> bool:
    color = [-1] * n
    for start in range(n):
        if color[start] != -1:
            continue
        color[start] = 0
        queue = deque([start])
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    queue.append(v)
                elif color[v] == color[u]:
                    return False
    return True


def is_bipartite_dfs(n: int, adj: List[List[int]]) -> bool:
    color = [-1] * n

    def dfs(u: int) -> bool:
        for v in adj[u]:
            if color[v] == -1:
                color[v] = color[u] ^ 1
                if not dfs(v):
                    return False
            elif color[v] == color[u]:
                return False
        return True

    for start in range(n):
        if color[start] == -1:
            color[start] = 0
            if not dfs(start):
                return False
    return True


if __name__ == "__main__":
    bipartite = [[1, 3], [0, 2], [1, 3], [0, 2]]
    not_bipartite = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
    assert is_bipartite_bfs(4, bipartite)
    assert is_bipartite_dfs(4, bipartite)
    assert not is_bipartite_bfs(4, not_bipartite)
    assert not is_bipartite_dfs(4, not_bipartite)
    print("[Python BipartiteCheck] BFS and DFS coloring verified.")
