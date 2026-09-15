"""LeetCode 9 - Palindrome Number."""
def palindrome_number(x):
    return x >= 0 and str(x) == str(x)[::-1]


if __name__ == "__main__":
    assert palindrome_number(121) is True
    assert palindrome_number(-121) is False
    assert palindrome_number(10) is False
    print("9 palindrome number ok")
