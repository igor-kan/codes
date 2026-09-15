"""Minimum cuts to partition a string into palindromes."""
def min_cut(s: str) -> int:
    n = len(s)
    is_pal = [[False] * n for _ in range(n)]
    cut = [0] * n
    for end in range(n):
        best = end
        for start in range(end + 1):
            if s[start] == s[end] and (end - start <= 1 or is_pal[start + 1][end - 1]):
                is_pal[start][end] = True
                best = 0 if start == 0 else min(best, cut[start - 1] + 1)
        cut[end] = best
    return cut[-1]


if __name__ == "__main__":
    assert min_cut("aab") == 1
    assert min_cut("abcbm") >= 2
    print("palindrome partition ok")
