"""Aggregator: collect correlated messages and emit one combined result."""
from __future__ import annotations

from collections import defaultdict


class OrderAggregator:
    def __init__(self, expected: int) -> None:
        self.expected = expected
        self._parts: dict[str, list[dict]] = defaultdict(list)

    def add(self, order_id: str, part: dict) -> dict | None:
        self._parts[order_id].append(part)
        if len(self._parts[order_id]) == self.expected:
            return {"orderId": order_id, "parts": self._parts.pop(order_id)}
        return None


if __name__ == "__main__":
    agg = OrderAggregator(expected=2)
    print(agg.add("o-1", {"kind": "invoice"}))
    print(agg.add("o-1", {"kind": "shipping"}))
