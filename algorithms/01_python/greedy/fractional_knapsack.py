"""Fractional knapsack (CLRS 16.2)."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Item:
    value: int
    weight: int


def fractional_knapsack(items: list[Item], capacity: int) -> float:
    total = 0.0
    remaining = capacity
    for item in sorted(items, key=lambda it: it.value / it.weight, reverse=True):
        if remaining <= 0:
            break
        take = min(item.weight, remaining)
        total += item.value * take / item.weight
        remaining -= take
    return total


if __name__ == "__main__":
    items = [Item(60, 10), Item(100, 20), Item(120, 30)]
    assert abs(fractional_knapsack(items, 50) - 240.0) < 1e-9
    print("fractional knapsack ok")
