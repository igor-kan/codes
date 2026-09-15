"""Regex matching with '.' and '*'."""
def is_match(text: str, pattern: str) -> bool:
    dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]
    dp[0][0] = True
    for j in range(2, len(pattern) + 1):
        if pattern[j - 1] == "*":
            dp[0][j] = dp[0][j - 2]
    for i in range(1, len(text) + 1):
        for j in range(1, len(pattern) + 1):
            if pattern[j - 1] in (".", text[i - 1]):
                dp[i][j] = dp[i - 1][j - 1]
            elif pattern[j - 1] == "*":
                dp[i][j] = dp[i][j - 2] or (
                    dp[i - 1][j] and pattern[j - 2] in (".", text[i - 1])
                )
    return dp[-1][-1]


if __name__ == "__main__":
    assert is_match("aab", "c*a*b")
    assert not is_match("mississippi", "mis*is*p*.")
    print("regex matching ok")
