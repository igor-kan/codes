"""Longest Palindromic Subsequence via dynamic programming."""

from typing import List


def longest_palindromic_subsequence(s: str) -> int:
    n = len(s)
    if n == 0:
        return 0
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    return dp[0][n - 1]


def longest_palindromic_subsequence_reconstruction(s: str) -> str:
    n = len(s)
    if n == 0:
        return ""
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    result = []
    i, j = 0, n - 1
    while i <= j:
        if s[i] == s[j]:
            result.append(s[i])
            i += 1
            j -= 1
        elif dp[i + 1][j] >= dp[i][j - 1]:
            i += 1
        else:
            j -= 1
    left = "".join(result)
    right = left[::-1]
    if dp[0][n - 1] % 2 == 1:
        right = right[1:]
    return left + right


if __name__ == "__main__":
    assert longest_palindromic_subsequence("bbbab") == 4
    assert longest_palindromic_subsequence("cbbd") == 2
    assert longest_palindromic_subsequence("a") == 1
    assert longest_palindromic_subsequence_reconstruction("bbbab") == "bbbb"
    assert longest_palindromic_subsequence_reconstruction("cbbd") == "bb"
    print("[Python LPS] Longest palindromic subsequence verified.")
