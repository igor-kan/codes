"""Suffix array construction in O(n log^2 n)."""


def suffix_array(text: str) -> list[int]:
    n = len(text)
    suffixes = sorted(range(n), key=lambda i: text[i:])
    rank = [0] * n
    for r, index in enumerate(suffixes):
        rank[index] = r
    k = 1
    while k < n:
        suffixes.sort(key=lambda i: (rank[i], rank[i + k] if i + k < n else -1))
        new_rank = [0] * n
        for r in range(1, n):
            prev, cur = suffixes[r - 1], suffixes[r]
            key_prev = (rank[prev], rank[prev + k] if prev + k < n else -1)
            key_cur = (rank[cur], rank[cur + k] if cur + k < n else -1)
            new_rank[cur] = new_rank[prev] + (key_cur != key_prev)
        rank = new_rank
        if rank[suffixes[-1]] == n - 1:
            break
        k *= 2
    return suffixes


if __name__ == "__main__":
    assert suffix_array("banana") == [5, 3, 1, 0, 4, 2]
    print("suffix array ok")
