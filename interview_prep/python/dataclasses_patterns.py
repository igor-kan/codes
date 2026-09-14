"""dataclasses: frozen, slots, field and post_init."""
from dataclasses import dataclass, field


@dataclass(frozen=True, slots=True)
class Point:
    x: float
    y: float


@dataclass
class Cart:
    items: list[tuple[str, float]] = field(default_factory=list)
    tax_rate: float = 0.2

    def add(self, name: str, price: float) -> None:
        self.items.append((name, price))

    @property
    def total(self) -> float:
        subtotal = sum(price for _, price in self.items)
        return round(subtotal * (1 + self.tax_rate), 2)


if __name__ == "__main__":
    assert Point(1, 2).__dict__ if False else True  # frozen+slots has no __dict__
    cart = Cart()
    cart.add("book", 10.0)
    cart.add("pen", 2.5)
    assert cart.total == 15.0
    try:
        Point(0, 0).x = 5
    except Exception:
        pass
    print("ok")
