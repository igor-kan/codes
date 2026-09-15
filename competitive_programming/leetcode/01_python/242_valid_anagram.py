"""LeetCode 242 - Valid Anagram."""
def valid_anagram(s, t):
    return sorted(s) == sorted(t)


if __name__ == "__main__":
    assert valid_anagram("anagram", "nagaram") is True
    assert valid_anagram("rat", "car") is False
    print("242 valid anagram ok")
