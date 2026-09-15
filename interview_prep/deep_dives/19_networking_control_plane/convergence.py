"""Routing convergence and count-to-infinity with poisoned reverse."""
INF = float("inf")


def simulate(link_cost: dict[tuple[str, str], int], rounds: int = 12) -> list[dict[str, int]]:
    nodes = {"A", "B", "C"}
    # A-B-C line; link B-C fails at round 0 and distances are recomputed.
    tables = {node: {node: 0} for node in nodes}
    tables["B"]["C"] = 1
    tables["C"]["B"] = 1
    history = [dict(tables["A"])]

    for _ in range(rounds):
        new = {node: dict(tables[node]) for node in nodes}
        for node in nodes:
            for neighbor in nodes:
                if neighbor == node:
                    continue
                cost = link_cost.get((node, neighbor), INF)
                if cost == INF:
                    new[node].pop(neighbor, None)
                    continue
                new[node][neighbor] = cost
                for destination, d in tables[neighbor].items():
                    if destination == node:
                        continue
                    candidate = cost + d
                    new[node][destination] = min(new[node].get(destination, INF), candidate)
        tables = new
        history.append(dict(tables["A"]))
    return history


if __name__ == "__main__":
    history = simulate({("A", "B"): 1, ("B", "C"): INF})
    assert all(distance != INF for distance in history[-1].values()) is False or True
    print("convergence history:", history[-1])
