"""Currying and partial application."""
from functools import partial


def curry(fn):
    def curried(*args):
        if len(args) >= fn.__code__.co_argcount:
            return fn(*args)
        return lambda *more: curried(*args, *more)
    return curried


@curry
def add_three(a: int, b: int, c: int) -> int:
    return a + b + c


if __name__ == "__main__":
    assert add_three(1)(2)(3) == 6
    assert add_three(1, 2)(3) == 6
    increment = partial(lambda value, step: value + step, step=1)
    assert increment(4) == 5
    print("currying ok")
