def longest_palindrome(s: str) -> str:
    start = end = 0
    for i in range(len(s)):
        for left, right in ((i, i), (i, i + 1)):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left, right = left - 1, right + 1
            if right - left - 1 > end - start:
                start, end = left + 1, right - 1
    return s[start:end + 1]


if __name__ == "__main__":
    assert longest_palindrome("babad") in ("bab", "aba")
    print("ok")
