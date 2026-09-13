# ==============================================================================
# File: languages/01_python/disjoint_set.py
# Language: Python 3.10+
# Domain: Combinatorial Algorithms & Graph Connectivity
# Algorithm: Disjoint Set Union (DSU / Union-Find) with Path Compression & Union by Rank
#
# Rationale & Language Fit:
#   Python's dynamic typing, clean slicing, and object-oriented abstractions
#   make combinatorial data structures intuitive and fast to prototype.
#   Path compression combined with union by rank guarantees an amortized time
#   complexity of O(alpha(N)) per operation, where alpha is the inverse Ackermann
#   function (effectively <= 4 for any physical input size).
# ==============================================================================

from typing import Generic, TypeVar, Dict, List, Optional

T = TypeVar("T")


class DisjointSetUnion(Generic[T]):
    """
    Production-grade Disjoint Set Union (DSU) data structure.
    Supports dynamic element registration, connected component tracking,
    path compression (halving/flattening), and union by rank/size.
    """

    def __init__(self):
        self._parent: Dict[T, T] = {}
        self._rank: Dict[T, int] = {}
        self._size: Dict[T, int] = {}
        self._num_components: int = 0

    def make_set(self, x: T) -> None:
        """Initializes a new singleton component containing x."""
        if x not in self._parent:
            self._parent[x] = x
            self._rank[x] = 0
            self._size[x] = 1
            self._num_components += 1

    def find(self, x: T) -> T:
        """
        Finds the canonical representative (root) of the set containing x.
        Applies full recursive path compression.
        """
        if x not in self._parent:
            self.make_set(x)
            return x

        # Two-pass path compression
        root = x
        while self._parent[root] != root:
            root = self._parent[root]

        curr = x
        while curr != root:
            nxt = self._parent[curr]
            self._parent[curr] = root
            curr = nxt

        return root

    def union(self, x: T, y: T) -> bool:
        """
        Merges the sets containing x and y.
        Uses union-by-rank to maintain balanced tree depths.
        Returns True if two distinct sets were merged, False if already connected.
        """
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        # Union by rank heuristic
        if self._rank[root_x] < self._rank[root_y]:
            root_x, root_y = root_y, root_x

        self._parent[root_y] = root_x
        self._size[root_x] += self._size[root_y]
        if self._rank[root_x] == self._rank[root_y]:
            self._rank[root_x] += 1

        self._num_components -= 1
        return True

    def connected(self, x: T, y: T) -> bool:
        """Returns True if x and y belong to the same equivalence class."""
        return self.find(x) == self.find(y)

    def component_size(self, x: T) -> int:
        """Returns the size of the connected component containing x."""
        return self._size[self.find(x)]

    @property
    def num_components(self) -> int:
        """Returns the total number of disjoint equivalence classes."""
        return self._num_components

    def get_components(self) -> Dict[T, List[T]]:
        """Returns a mapping from canonical root to list of all member elements."""
        groups: Dict[T, List[T]] = {}
        for elem in self._parent:
            root = self.find(elem)
            groups.setdefault(root, []).append(elem)
        return groups


# --- Demonstration & Verification ---
if __name__ == "__main__":
    print("=================================================================")
    print("Python Disjoint Set Union (DSU / Union-Find Engine)")
    print("=================================================================\n")

    dsu = DisjointSetUnion[int]()

    # Create 10 nodes (0 to 9)
    for i in range(10):
        dsu.make_set(i)

    print(f"Initial components: {dsu.num_components}")

    # Add edges: (0, 1), (1, 2), (3, 4), (4, 5), (6, 7), (8, 9)
    edges = [(0, 1), (1, 2), (3, 4), (4, 5), (6, 7), (8, 9)]
    for u, v in edges:
        dsu.union(u, v)

    print(f"Components after initial batch: {dsu.num_components}")
    assert dsu.connected(0, 2) is True
    assert dsu.connected(0, 3) is False
    assert dsu.component_size(0) == 3

    # Merge component {0, 1, 2} with component {3, 4, 5}
    dsu.union(2, 3)
    assert dsu.connected(0, 5) is True
    assert dsu.component_size(0) == 6
    print(f"Merged component size: {dsu.component_size(0)}")
    print(f"All components: {dsu.get_components()}")
    print("\n[SUCCESS] DSU path compression and union-by-rank verified.")
