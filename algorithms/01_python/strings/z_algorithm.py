"""Z-algorithm for linear-time pattern matching."""

from typing import List


def z_function(s: str) -> List[int]:
    n = len(s)
    z = [0] * n
    l = r = 0
    for i in range(1, n):
        if i < r:
            z[i] = min(r - i, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > r:
            l, r = i, i + z[i]
    z[0] = n
    return z


def z_search(text: str, pattern: str) -> List[int]:
    """0-based start indices of all occurrences of pattern in text."""
    if not pattern:
        return []
    combined = pattern + "#" + text
    z = z_function(combined)
    m = len(pattern)
    return [i - m - 1 for i in range(m + 1, len(combined)) if z[i] == m]


if __name__ == "__main__":
    assert z_function("aaaa") == [4, 3, 2, 1]
    assert z_function("abacaba") == [7, 0, 1, 0, 3, 0, 1]

    assert z_search("ABABDABACDABABCABAB", "ABAB") == [0, 10, 15]
    assert z_search("aaaa", "aa") == [0, 1, 2]
    assert z_search("hello", "ll") == [2]
    assert z_search("hello", "xyz") == []
    print("[Python ZAlgorithm] Pattern matching verified.")
