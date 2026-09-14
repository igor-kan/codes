"""Content-Based Router: dispatch on message content/type."""
from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass


@dataclass(frozen=True)
class Order:
    kind: str
    amount: float


def route(order: Order) -> str:
    if order.amount > 10_000:
        return "manual-review"
    match order.kind:
        case "digital":
            return "instant-fulfilment"
        case "physical":
            return "warehouse"
        case _:
            return "unrouted"


if __name__ == "__main__":
    for order in (Order("digital", 20), Order("physical", 50), Order("physical", 50_000)):
        print(order, "->", route(order))
