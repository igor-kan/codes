"""
Hopcroft-Karp Algorithm in Python.
Maximum cardinality bipartite matching in O(E sqrt(V)).
"""

from collections import deque

class HopcroftKarp:
    def __init__(self, nu, nv, adj):
        self.nu = nu
        self.nv = nv
        self.adj = adj
        self.pair_u = [0] * (nu + 1)
        self.pair_v = [0] * (nv + 1)
        self.dist = [0] * (nu + 1)

    def max_matching(self):
        matching = 0
        while self._bfs():
            for u in range(1, self.nu + 1):
                if self.pair_u[u] == 0 and self._dfs(u):
                    matching += 1
        return matching

    def _bfs(self):
        q = deque()
        for u in range(1, self.nu + 1):
            if self.pair_u[u] == 0:
                self.dist[u] = 0
                q.append(u)
            else:
                self.dist[u] = float('inf')
        self.dist[0] = float('inf')

        while q:
            u = q.popleft()
            if self.dist[u] < self.dist[0]:
                for v in self.adj[u]:
                    if self.dist[self.pair_v[v]] == float('inf'):
                        self.dist[self.pair_v[v]] = self.dist[u] + 1
                        q.append(self.pair_v[v])
        return self.dist[0] != float('inf')

    def _dfs(self, u):
        if u != 0:
            for v in self.adj[u]:
                if self.dist[self.pair_v[v]] == self.dist[u] + 1 and self._dfs(self.pair_v[v]):
                    self.pair_v[v] = u
                    self.pair_u[u] = v
                    return True
            self.dist[u] = float('inf')
            return False
        return True

if __name__ == "__main__":
    adj = [[], [2, 3], [1], [2], [2, 4]]
    hk = HopcroftKarp(4, 4, adj)
    assert hk.max_matching() == 4
    print("Python Hopcroft-Karp verified.")
