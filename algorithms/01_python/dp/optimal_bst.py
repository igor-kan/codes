"""Optimal binary search tree cost."""
def optimal_bst(keys: list[int], freq: list[int]) -> int:
    n = len(keys)
    cost = [[0] * n for _ in range(n)]
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + freq[i]
    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            best = float("inf")
            for r in range(i, j + 1):
                left = cost[i][r - 1] if r > i else 0
                right = cost[r + 1][j] if r < j else 0
                best = min(best, left + right)
            cost[i][j] = best + (prefix[j + 1] - prefix[i])
    return cost[0][n - 1]


if __name__ == "__main__":
    assert optimal_bst([10, 12, 20], [34, 8, 50]) == 142
    print("optimal bst ok")
