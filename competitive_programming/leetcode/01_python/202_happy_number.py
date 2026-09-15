"""LeetCode 202 - Happy Number."""
def happy_number(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1


if __name__ == "__main__":
    assert happy_number(19) is True
    assert happy_number(2) is False
    print("202 happy number ok")
