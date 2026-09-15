"""Ford-Fulkerson max flow with DFS augmenting paths."""
def ford_fulkerson(capacity: list[list[int]], source: int, sink: int) -> int:
    n = len(capacity)
    residual = [row[:] for row in capacity]
    flow = 0

    def dfs(u: int, limit: float, visited: list[bool]) -> float:
        if u == sink:
            return limit
        visited[u] = True
        for v in range(n):
            if not visited[v] and residual[u][v] > 0:
                pushed = dfs(v, min(limit, residual[u][v]), visited)
                if pushed:
                    residual[u][v] -= pushed
                    residual[v][u] += pushed
                    return pushed
        return 0

    while True:
        pushed = dfs(source, float("inf"), [False] * n)
        if not pushed:
            break
        flow += pushed
    return int(flow)


if __name__ == "__main__":
    capacity = [[0, 10, 10, 0], [0, 0, 2, 8], [0, 0, 0, 10], [0, 0, 0, 0]]
    assert ford_fulkerson(capacity, 0, 3) == 18
    print("ford-fulkerson ok")
