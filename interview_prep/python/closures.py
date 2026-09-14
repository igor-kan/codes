"""Closures, cells and late binding."""
from functools import partial


def counter():
    count = 0

    def increment(step: int = 1) -> int:
        nonlocal count
        count += step
        return count
    return increment


def clamp(lo: int, hi: int, value: int) -> int:
    return max(lo, min(hi, value))


if __name__ == "__main__":
    c = counter()
    assert (c(), c(2), c()) == (1, 3, 4)

    clamp_0_10 = partial(clamp, 0, 10)
    assert clamp_0_10(15) == 10

    funcs = [lambda x, i=i: x + i for i in range(3)]
    assert [f(10) for f in funcs] == [10, 11, 12]
    print("ok")
