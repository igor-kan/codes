"""LeetCode 69 - Sqrt(x)."""
def sqrt_x(x):
    low, high = 0, x
    while low <= high:
        middle = (low + high) // 2
        if middle * middle <= x:
            low = middle + 1
        else:
            high = middle - 1
    return high


if __name__ == "__main__":
    assert sqrt_x(4) == 2
    assert sqrt_x(8) == 2
    assert sqrt_x(0) == 0
    assert sqrt_x(2147395599) == 46339
    print("69 sqrt x ok")
