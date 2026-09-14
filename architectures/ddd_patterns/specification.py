"""Specification: compose business rules as reusable predicates."""
from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass(frozen=True)
class Specification(Generic[T]):
    predicate: Callable[[T], bool]

    def __and__(self, other: "Specification[T]") -> "Specification[T]":
        return Specification(lambda item: self.predicate(item) and other.predicate(item))

    def __or__(self, other: "Specification[T]") -> "Specification[T]":
        return Specification(lambda item: self.predicate(item) or other.predicate(item))

    def __invert__(self) -> "Specification[T]":
        return Specification(lambda item: not self.predicate(item))

    def is_satisfied_by(self, candidate: T) -> bool:
        return self.predicate(candidate)


@dataclass
class Invoice:
    total: int
    paid: bool


if __name__ == "__main__":
    over_threshold = Specification[Invoice](lambda i: i.total > 10_000)
    unpaid = Specification[Invoice](lambda i: not i.paid)
    risky = over_threshold & unpaid
    print(risky.is_satisfied_by(Invoice(20_000, paid=False)))
    print((~unpaid).is_satisfied_by(Invoice(20_000, paid=True)))
