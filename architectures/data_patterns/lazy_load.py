"""Lazy Load: defer an expensive attribute until first access."""
class Lazy:
    def __init__(self, loader) -> None:
        self._loader = loader
        self._loaded = False
        self._value = None

    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        if not self._loaded:
            self._value = self._loader(instance)
            self._loaded = True
        return self._value


class Customer:
    def __init__(self, customer_id: int) -> None:
        self.customer_id = customer_id

    def _load_orders(self) -> list[str]:
        return [f"order-{self.customer_id}->{i}" for i in range(3)]

    orders = Lazy(_load_orders)


if __name__ == "__main__":
    customer = Customer(7)
    assert customer.orders == ["order-7->0", "order-7->1", "order-7->2"]
    print("lazy load ok")
