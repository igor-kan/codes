"""LeetCode 28 - Find the Index of the First Occurrence in a String."""
def str_str(haystack, needle):
    return haystack.find(needle)


if __name__ == "__main__":
    assert str_str("sadbutsad", "sad") == 0
    assert str_str("leetcode", "leeto") == -1
    print("28 find index first occurrence ok")
