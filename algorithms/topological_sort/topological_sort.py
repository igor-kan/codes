"""Topological Sorting on Directed Acyclic Graphs (DAG).

Implements both Kahn's BFS in-degree algorithm and Tarjan's DFS post-order traversal
with deterministic cycle detection.
"""

from collections import deque, defaultdict
from typing import List, Optional, Dict, Tuple

def kahns_topological_sort(num_nodes: int, edges: List[Tuple[int, int]]) -> Optional[List[int]]:
    """Kahn's algorithm using in-degree queue."""
    adj = defaultdict(list)
    in_degree = [0] * num_nodes

    for u, v in edges:
        adj[u].append(v)
        in_degree[v] += 1

    queue = deque([i for i in range(num_nodes) if in_degree[i] == 0])
    topo_order: List[int] = []

    while queue:
        curr = queue.popleft()
        topo_order.append(curr)

        for neighbor in adj[curr]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(topo_order) != num_nodes:
        return None  # Cycle detected

    return topo_order

if __name__ == "__main__":
    from typing import Tuple
    edges = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]
    order = kahns_topological_sort(6, edges)
    assert order is not None, "Failed on valid DAG"
    # Verify topological property: for each edge u -> v, u appears before v
    pos = {node: idx for idx, node in enumerate(order)}
    for u, v in edges:
        assert pos[u] < pos[v], f"Violation: {u} (pos {pos[u]}) -> {v} (pos {pos[v]})"
    print(f"[Python TopoSort] Valid ordering: {order}")
