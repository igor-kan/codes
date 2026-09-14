"""Descriptors: managed attributes."""
import logging


class Validated:
    def __init__(self, minimum: int) -> None:
        self.minimum = minimum
        self.name = None

    def __set_name__(self, owner, name: str) -> None:
        self.name = name

    def __get__(self, obj, owner=None):
        if obj is None:
            return self
        return obj.__dict__[self.name]

    def __set__(self, obj, value: int) -> None:
        if value < self.minimum:
            raise ValueError(f"{self.name} must be >= {self.minimum}")
        obj.__dict__[self.name] = value


class Order:
    quantity = Validated(minimum=1)

    def __init__(self, quantity: int) -> None:
        self.quantity = quantity


if __name__ == "__main__":
    order = Order(3)
    assert order.quantity == 3
    try:
        Order(0)
    except ValueError as exc:
        assert "quantity" in str(exc)
    else:
        raise AssertionError("expected ValueError")
    print("ok")
