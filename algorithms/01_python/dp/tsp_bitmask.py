"""Travelling salesman with bitmask DP."""
def tsp(distance: list[list[int]]) -> int:
    n = len(distance)
    full = 1 << n
    dp = [[float("inf")] * n for _ in range(full)]
    dp[1][0] = 0
    for mask in range(full):
        for u in range(n):
            if not dp[mask][u] < float("inf"):
                continue
            for v in range(n):
                if mask & (1 << v):
                    continue
                new_mask = mask | (1 << v)
                dp[new_mask][v] = min(dp[new_mask][v], dp[mask][u] + distance[u][v])
    best = float("inf")
    last = full - 1
    for u in range(1, n):
        best = min(best, dp[last][u] + distance[u][0])
    return int(best)


if __name__ == "__main__":
    dist = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0],
    ]
    assert tsp(dist) == 80
    print("tsp bitmask ok")
