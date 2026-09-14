"""Functional building blocks."""
from functools import reduce
from operator import add, mul
from itertools import starmap


def compose(*funcs):
    def composed(value):
        for fn in reversed(funcs):
            value = fn(value)
        return value
    return composed


if __name__ == "__main__":
    assert reduce(add, [1, 2, 3, 4]) == 10
    assert reduce(mul, range(1, 6)) == 120
    pipeline = compose(lambda x: x + 1, lambda x: x * 2)
    assert pipeline(3) == 7
    assert list(starmap(pow, [(2, 3), (3, 2)])) == [8, 9]
    print("ok")
