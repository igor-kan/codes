"""Value Object: immutable, compared by value."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Money:
    amount_minor: int
    currency: str

    def __post_init__(self) -> None:
        if self.amount_minor < 0:
            raise ValueError("amount must be non-negative")
        if len(self.currency) != 3:
            raise ValueError("currency must be an ISO-4217 code")

    def plus(self, other: "Money") -> "Money":
        if self.currency != other.currency:
            raise ValueError("currency mismatch")
        return Money(self.amount_minor + other.amount_minor, self.currency)

    def __str__(self) -> str:
        return f"{self.amount_minor / 100:.2f} {self.currency}"


if __name__ == "__main__":
    print(Money(1050, "USD").plus(Money(250, "USD")))
