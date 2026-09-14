"""Splitter: turn one message into many downstream messages."""
from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass


@dataclass(frozen=True)
class Order:
    id: str
    items: list[str]


def split(order: Order) -> Iterator[dict]:
    for index, item in enumerate(order.items):
        yield {"orderId": order.id, "line": index, "sku": item}


if __name__ == "__main__":
    for message in split(Order("o-1", ["book", "pen", "lamp"])):
        print(message)
