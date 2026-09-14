"""Generics, TypeVar, ParamSpec and overloads."""
from collections.abc import Callable, Iterable
from typing import TypeVar, overload

T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")


def first(items: Iterable[T]) -> T | None:
    return next(iter(items), None)


def group_by(items: Iterable[T], key: Callable[[T], K]) -> dict[K, list[T]]:
    result: dict[K, list[T]] = {}
    for item in items:
        result.setdefault(key(item), []).append(item)
    return result


@overload
def parse(value: str) -> str: ...
@overload
def parse(value: int) -> int: ...
def parse(value):
    return value


if __name__ == "__main__":
    assert first([1, 2, 3]) == 1
    assert group_by(["a", "bb", "cc"], len) == {1: ["a"], 2: ["bb", "cc"]}
    assert parse("x") == "x"
    print("ok")
