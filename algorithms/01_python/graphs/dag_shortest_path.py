"""Single-source shortest paths in a DAG, O(V + E) (CLRS 24.2)."""
INF = float("inf")


def dag_shortest_paths(adjacency: dict[str, list[tuple[str, int]]], source: str) -> dict[str, float]:
    order: list[str] = []
    visited: set[str] = set()

    def visit(node: str) -> None:
        visited.add(node)
        for nxt, _ in adjacency.get(node, []):
            if nxt not in visited:
                visit(nxt)
        order.append(node)

    for node in adjacency:
        if node not in visited:
            visit(node)
    order.reverse()

    dist = {node: INF for node in adjacency}
    dist[source] = 0
    for node in order:
        if dist[node] == INF:
            continue
        for nxt, weight in adjacency.get(node, []):
            if dist[node] + weight < dist[nxt]:
                dist[nxt] = dist[node] + weight
    return dist


if __name__ == "__main__":
    graph = {
        "r": [("s", 5), ("t", 3)],
        "s": [("t", 2), ("x", 6)],
        "t": [("x", 7), ("y", 4), ("z", 2)],
        "x": [("y", -1), ("z", 1)],
        "y": [("z", -2)],
        "z": [],
    }
    dist = dag_shortest_paths(graph, "s")
    assert dist["z"] == 3 and dist["y"] == 5 and dist["x"] == 6
    print("dag shortest path ok")
