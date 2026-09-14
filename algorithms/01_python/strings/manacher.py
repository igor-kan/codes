"""Manacher's algorithm for longest palindromic substring in O(n)."""

from typing import List


def manacher(s: str) -> str:
    t = "#" + "#".join(s) + "#"
    n = len(t)
    p = [0] * n
    center = right = 0
    for i in range(n):
        mirror = 2 * center - i
        if i < right:
            p[i] = min(right - i, p[mirror])
        while i - p[i] - 1 >= 0 and i + p[i] + 1 < n and t[i - p[i] - 1] == t[i + p[i] + 1]:
            p[i] += 1
        if i + p[i] > right:
            center, right = i, i + p[i]

    max_len = max(p)
    center_idx = p.index(max_len)
    start = (center_idx - max_len) // 2
    return s[start:start + max_len]


if __name__ == "__main__":
    assert manacher("babad") == "bab" or manacher("babad") == "aba"
    assert manacher("cbbd") == "bb"
    assert manacher("a") == "a"
    assert manacher("racecar") == "racecar"
    assert manacher("") == ""
    print("[Python Manacher] Longest palindromic substring verified.")
