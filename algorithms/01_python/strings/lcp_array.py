"""Kasai's algorithm for the LCP array from a suffix array."""
def suffix_array(text: str) -> list[int]:
    return sorted(range(len(text)), key=lambda i: text[i:])


def lcp_array(text: str, suffixes: list[int]) -> list[int]:
    n = len(text)
    rank = [0] * n
    for r, index in enumerate(suffixes):
        rank[index] = r
    lcp = [0] * n
    length = 0
    for i in range(n):
        if rank[i] > 0:
            j = suffixes[rank[i] - 1]
            while i + length < n and j + length < n and text[i + length] == text[j + length]:
                length += 1
            lcp[rank[i]] = length
            length = max(length - 1, 0)
    return lcp


if __name__ == "__main__":
    text = "banana"
    suffixes = suffix_array(text)
    assert lcp_array(text, suffixes) == [0, 1, 3, 0, 0, 2]
    print("lcp array ok")
