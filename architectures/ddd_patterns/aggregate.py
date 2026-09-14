"""Aggregate: a consistency boundary with a single entry point."""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class OrderLine:
    sku: str
    quantity: int
    unit_price: int


@dataclass
class Order:  # aggregate root
    id: str
    lines: list[OrderLine] = field(default_factory=list)
    status: str = "draft"
    _events: list[dict] = field(default_factory=list)

    def add_line(self, sku: str, quantity: int, unit_price: int) -> None:
        if self.status != "draft":
            raise ValueError("cannot modify a submitted order")
        if quantity <= 0:
            raise ValueError("quantity must be positive")
        self.lines.append(OrderLine(sku, quantity, unit_price))

    def submit(self) -> None:
        if not self.lines:
            raise ValueError("cannot submit an empty order")
        self.status = "submitted"
        self._events.append({"type": "OrderSubmitted", "orderId": self.id})

    @property
    def total(self) -> int:
        return sum(line.quantity * line.unit_price for line in self.lines)

    def pull_events(self) -> list[dict]:
        events, self._events = self._events, []
        return events


if __name__ == "__main__":
    order = Order("o-1")
    order.add_line("book", 2, 1200)
    order.submit()
    print(order.total, order.status, order.pull_events())
