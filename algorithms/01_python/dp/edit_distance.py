def edit_distance(a, b):
    m, n = len(a), len(b)
    dp = list(range(n+1))
    for i in range(1, m+1):
        prev, dp[0] = dp[0], i
        for j in range(1, n+1):
            prev, dp[j] = dp[j], min(
                dp[j] + 1, dp[j-1] + 1,
                prev + (0 if a[i-1] == b[j-1] else 1)
            )
    return dp[n]
