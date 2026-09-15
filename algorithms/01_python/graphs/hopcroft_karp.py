"""Hopcroft-Karp maximum bipartite matching."""
from collections import deque

INF = float("inf")


def hopcroft_karp(adjacency: list[list[int]], left_size: int, right_size: int) -> int:
    pair_u = [-1] * left_size
    pair_v = [-1] * right_size
    dist = [0] * left_size

    def bfs() -> bool:
        queue = deque()
        for u in range(left_size):
            if pair_u[u] == -1:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = INF
        found = False
        while queue:
            u = queue.popleft()
            for v in adjacency[u]:
                w = pair_v[v]
                if w == -1:
                    found = True
                elif dist[w] == INF:
                    dist[w] = dist[u] + 1
                    queue.append(w)
        return found

    def dfs(u: int) -> bool:
        for v in adjacency[u]:
            w = pair_v[v]
            if w == -1 or (dist[w] == dist[u] + 1 and dfs(w)):
                pair_u[u], pair_v[v] = v, u
                return True
        dist[u] = INF
        return False

    matching = 0
    while bfs():
        for u in range(left_size):
            if pair_u[u] == -1 and dfs(u):
                matching += 1
    return matching


if __name__ == "__main__":
    adjacency = [[0, 1], [0], [1, 2], [2]]
    assert hopcroft_karp(adjacency, 4, 3) == 3
    print("hopcroft-karp ok")
