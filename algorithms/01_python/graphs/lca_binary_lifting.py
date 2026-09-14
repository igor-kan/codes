"""Lowest Common Ancestor via binary lifting."""

from typing import List


class LCA:
    def __init__(self, n: int, edges: List[List[int]], root: int = 0):
        self.n = n
        self.LOG = (n).bit_length()
        self.up = [[-1] * n for _ in range(self.LOG)]
        self.depth = [0] * n

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        self._dfs(root, -1, adj)

    def _dfs(self, u: int, parent: int, adj: List[List[int]]):
        self.up[0][u] = parent
        for v in adj[u]:
            if v == parent:
                continue
            self.depth[v] = self.depth[u] + 1
            self._dfs(v, u, adj)

        for k in range(1, self.LOG):
            mid = self.up[k - 1][u]
            self.up[k][u] = -1 if mid == -1 else self.up[k - 1][mid]

    def lca(self, u: int, v: int) -> int:
        if self.depth[u] < self.depth[v]:
            u, v = v, u
        diff = self.depth[u] - self.depth[v]
        for k in range(self.LOG):
            if diff & (1 << k):
                u = self.up[k][u]
        if u == v:
            return u
        for k in range(self.LOG - 1, -1, -1):
            if self.up[k][u] != self.up[k][v]:
                u = self.up[k][u]
                v = self.up[k][v]
        return self.up[0][u]

    def dist(self, u: int, v: int) -> int:
        return self.depth[u] + self.depth[v] - 2 * self.depth[self.lca(u, v)]


if __name__ == "__main__":
    edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]]
    lca = LCA(7, edges)
    assert lca.lca(3, 4) == 1
    assert lca.lca(3, 6) == 0
    assert lca.lca(5, 6) == 2
    assert lca.lca(3, 3) == 3
    assert lca.dist(3, 4) == 2
    assert lca.dist(3, 6) == 4
    print("[Python LCA] Binary lifting verified.")
