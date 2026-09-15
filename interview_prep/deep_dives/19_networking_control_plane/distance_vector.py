"""Distance-vector routing with Bellman-Ford and count-to-infinity."""
INF = float("inf")


def update(routes: dict[str, int], neighbors: dict[str, dict[str, int]], node: str) -> dict[str, int]:
    table = {node: 0}
    for destination in routes:
        best = routes.get(destination, INF)
        for neighbor, cost in neighbors.items():
            candidate = cost + routes.get(destination, INF)
            if candidate < best:
                best = candidate
        if best != INF:
            table[destination] = best
    return table


def converges(routers: dict[str, dict[str, dict[str, int]]], rounds: int = 10):
    tables = {node: {node: 0} for node in routers}
    for _ in range(rounds):
        updated = {}
        for node, neighbors in routers.items():
            merged = dict(tables[node])
            for destination in {d for t in tables.values() for d in t}:
                best = merged.get(destination, INF)
                for neighbor, cost in neighbors.items():
                    if neighbor == destination:
                        best = min(best, cost)
                        continue
                    candidate = cost + tables[neighbor].get(destination, INF)
                    best = min(best, candidate)
                if best != INF:
                    merged[destination] = best
            updated[node] = merged
        if updated == tables:
            break
        tables = updated
    return tables


if __name__ == "__main__":
    routers = {
        "A": {"B": 1},
        "B": {"A": 1, "C": 1},
        "C": {"B": 1},
    }
    tables = converges(routers)
    assert tables["A"]["C"] == 2
    print("distance vector converged:", tables["A"])
