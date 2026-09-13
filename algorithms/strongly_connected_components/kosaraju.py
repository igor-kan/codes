from typing import Dict, List


class KosarajuSCC:
    def __init__(self, num_nodes: int):
        self.n = num_nodes
        self.adj: List[List[int]] = [[] for _ in range(num_nodes)]
        self.rev_adj: List[List[int]] = [[] for _ in range(num_nodes)]

    def add_edge(self, u: int, v: int):
        self.adj[u].append(v)
        self.rev_adj[v].append(u)

    def find_sccs(self) -> List[List[int]]:
        order = []
        visited = [False] * self.n

        def dfs1(u: int):
            visited[u] = True
            for v in self.adj[u]:
                if not visited[v]:
                    dfs1(v)
            order.append(u)

        for i in range(self.n):
            if not visited[i]:
                dfs1(i)

        visited = [False] * self.n
        sccs = []

        def dfs2(u: int, component: List[int]):
            visited[u] = True
            component.append(u)
            for v in self.rev_adj[u]:
                if not visited[v]:
                    dfs2(v, component)

        for u in reversed(order):
            if not visited[u]:
                component = []
                dfs2(u, component)
                sccs.append(component)

        return sccs


if __name__ == "__main__":
    g = KosarajuSCC(5)
    g.add_edge(1, 0)
    g.add_edge(0, 2)
    g.add_edge(2, 1)
    g.add_edge(0, 3)
    g.add_edge(3, 4)

    sccs = g.find_sccs()
    assert len(sccs) == 3
    print(f"[Python SCC] Discovered {len(sccs)} components: {sccs}")
