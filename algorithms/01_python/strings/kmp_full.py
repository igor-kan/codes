"""Knuth-Morris-Pratt (KMP) Linear Time String Search Algorithm.

Precomputes the longest proper prefix which is also a suffix (LPS table)
to achieve deterministic O(N + M) substring pattern matching.
"""

from typing import List

def compute_lps(pattern: str) -> List[int]:
    """Computes the π prefix table for pattern."""
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(text: str, pattern: str) -> List[int]:
    """Returns 0-based start indices of all occurrences of pattern in text."""
    if not pattern or not text:
        return []

    n, m = len(text), len(pattern)
    lps = compute_lps(pattern)
    occurrences: List[int] = []

    i = 0  # index in text
    j = 0  # index in pattern

    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == m:
            occurrences.append(i - j)
            j = lps[j - 1]
        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return occurrences

if __name__ == "__main__":
    txt = "ABABDABACDABABCABABABABCABAB"
    pat = "ABABCABAB"
    matches = kmp_search(txt, pat)
    assert matches == [10, 19], f"Unexpected matches: {matches}"
    print(f"[Python KMP] Pattern found at occurrences: {matches}")
