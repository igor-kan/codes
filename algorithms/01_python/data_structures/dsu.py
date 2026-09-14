"""Disjoint Set Union (Union-Find) with path compression and union by size."""


class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
        self.components = n

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> bool:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        self.components -= 1
        return True

    def connected(self, a: int, b: int) -> bool:
        return self.find(a) == self.find(b)


if __name__ == "__main__":
    dsu = DSU(6)
    assert dsu.components == 6
    assert dsu.union(0, 1)
    assert dsu.union(1, 2)
    assert dsu.union(3, 4)
    assert dsu.connected(0, 2)
    assert dsu.connected(3, 4)
    assert not dsu.connected(0, 3)
    assert not dsu.union(0, 2)
    assert dsu.components == 3
    assert dsu.union(2, 3)
    assert dsu.connected(0, 4)
    print("[Python DSU] Union-Find verified.")
