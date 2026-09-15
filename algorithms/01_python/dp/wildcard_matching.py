"""Wildcard matching with '?' (single) and '*' (any sequence)."""
def is_match(text: str, pattern: str) -> bool:
    dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]
    dp[0][0] = True
    for j in range(1, len(pattern) + 1):
        if pattern[j - 1] == "*":
            dp[0][j] = dp[0][j - 1]
    for i in range(1, len(text) + 1):
        for j in range(1, len(pattern) + 1):
            if pattern[j - 1] in ("?", text[i - 1]):
                dp[i][j] = dp[i - 1][j - 1]
            elif pattern[j - 1] == "*":
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
    return dp[-1][-1]


if __name__ == "__main__":
    assert is_match("adceb", "*a*b")
    assert not is_match("acdcb", "a*c?b")
    print("wildcard matching ok")
