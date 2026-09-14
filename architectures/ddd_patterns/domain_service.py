"""Domain Service: stateless operation that spans multiple aggregates."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Account:
    id: str
    balance: int


class TransferService:
    """Pure domain logic operating on aggregates; persistence lives elsewhere."""

    def transfer(self, source: Account, target: Account, amount: int) -> tuple[Account, Account]:
        if amount <= 0:
            raise ValueError("amount must be positive")
        if source.balance < amount:
            raise ValueError("insufficient funds")
        return (
            Account(source.id, source.balance - amount),
            Account(target.id, target.balance + amount),
        )


if __name__ == "__main__":
    service = TransferService()
    print(service.transfer(Account("a", 100), Account("b", 0), 40))
