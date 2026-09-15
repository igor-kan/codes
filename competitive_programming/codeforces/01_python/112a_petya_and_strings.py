"""Codeforces 112A - Petya and Strings."""
def petya_and_strings(a, b):
    left, right = a.lower(), b.lower()
    if left < right:
        return -1
    if left > right:
        return 1
    return 0


if __name__ == "__main__":
    assert petya_and_strings("aaaa", "aaaA") == 0
    assert petya_and_strings("abs", "Abz") == -1
    assert petya_and_strings("abcdefg", "AbCdEfF") == 1
    print("112A petya and strings ok")
