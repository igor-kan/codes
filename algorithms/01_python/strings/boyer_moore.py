"""Boyer-Moore-Horspool substring search."""
def boyer_moore(text: str, pattern: str) -> int:
    if not pattern:
        return 0
    m = len(pattern)
    skip = {ch: m for ch in set(pattern)}
    for i in range(m - 1):
        skip[pattern[i]] = m - 1 - i
    i = 0
    while i <= len(text) - m:
        j = m - 1
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1
        if j < 0:
            return i
        i += skip.get(text[i + m - 1], m)
    return -1


if __name__ == "__main__":
    assert boyer_moore("here is a simple example", "example") == 17
    assert boyer_moore("abc", "xyz") == -1
    print("boyer-moore ok")
