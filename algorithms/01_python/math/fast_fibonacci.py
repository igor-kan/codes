"""Fibonacci via fast doubling (O(log n))."""
def fib(n: int) -> int:
    def helper(k: int) -> tuple[int, int]:
        if k == 0:
            return 0, 1
        a, b = helper(k >> 1)
        c = a * (2 * b - a)
        d = a * a + b * b
        return (d, c + d) if k & 1 else (c, d)

    return helper(n)[0]


def fib_pair(n: int) -> tuple[int, int]:
    def helper(k: int) -> tuple[int, int]:
        if k == 0:
            return 0, 1
        a, b = helper(k // 2)
        c = a * (2 * b - a)
        d = a * a + b * b
        return (c, d) if k % 2 == 0 else (d, c + d)

    return helper(n)


if __name__ == "__main__":
    assert [fib(i) for i in range(11)] == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    assert fib(90) == 2880067194370816120
    print("fast fibonacci ok")
