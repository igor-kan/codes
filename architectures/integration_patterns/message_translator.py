"""Message Translator: convert between message formats."""
from dataclasses import dataclass


@dataclass(frozen=True)
class LegacyOrder:
    order_no: str
    total_cents: int


@dataclass(frozen=True)
class ModernOrder:
    id: str
    total: float
    currency: str = "USD"


def translate(message: LegacyOrder) -> ModernOrder:
    return ModernOrder(id=message.order_no, total=message.total_cents / 100)


if __name__ == "__main__":
    assert translate(LegacyOrder("A-1", 1999)) == ModernOrder("A-1", 19.99)
    print("message translator ok")
