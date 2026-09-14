"""Dinic's maximum flow algorithm."""

from collections import deque
from typing import List


class Dinic:
    def __init__(self, n: int):
        self.n = n
        self.adj: List[List[List[int]]] = [[] for _ in range(n)]

    def add_edge(self, u: int, v: int, cap: int):
        self.adj[u].append([v, cap, len(self.adj[v])])
        self.adj[v].append([u, 0, len(self.adj[u]) - 1])

    def _bfs(self, s: int, t: int) -> bool:
        self.level = [-1] * self.n
        queue = deque([s])
        self.level[s] = 0
        while queue:
            u = queue.popleft()
            for v, cap, _ in self.adj[u]:
                if cap > 0 and self.level[v] == -1:
                    self.level[v] = self.level[u] + 1
                    queue.append(v)
        return self.level[t] != -1

    def _dfs(self, u: int, t: int, pushed: int) -> int:
        if u == t:
            return pushed
        while self.it[u] < len(self.adj[u]):
            v, cap, rev = self.adj[u][self.it[u]]
            if cap > 0 and self.level[v] == self.level[u] + 1:
                tr = self._dfs(v, t, min(pushed, cap))
                if tr > 0:
                    self.adj[u][self.it[u]][1] -= tr
                    self.adj[v][rev][1] += tr
                    return tr
            self.it[u] += 1
        return 0

    def max_flow(self, s: int, t: int) -> int:
        flow = 0
        INF = float("inf")
        while self._bfs(s, t):
            self.it = [0] * self.n
            while True:
                pushed = self._dfs(s, t, INF)
                if pushed == 0:
                    break
                flow += pushed
        return flow


if __name__ == "__main__":
    dinic = Dinic(6)
    dinic.add_edge(0, 1, 16)
    dinic.add_edge(0, 2, 13)
    dinic.add_edge(1, 2, 10)
    dinic.add_edge(1, 3, 12)
    dinic.add_edge(2, 1, 4)
    dinic.add_edge(2, 4, 14)
    dinic.add_edge(3, 2, 9)
    dinic.add_edge(3, 5, 20)
    dinic.add_edge(4, 3, 7)
    dinic.add_edge(4, 5, 4)
    assert dinic.max_flow(0, 5) == 23
    print("[Python Dinic] Max flow verified.")
