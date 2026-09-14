"""Repository: collection-like access to aggregates, hiding persistence."""
from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True)
class Account:
    id: str
    owner: str
    balance: int


class AccountRepository(ABC):
    @abstractmethod
    def get(self, account_id: str) -> Account | None: ...

    @abstractmethod
    def save(self, account: Account) -> None: ...


class InMemoryAccountRepository(AccountRepository):
    def __init__(self) -> None:
        self._store: dict[str, Account] = {}

    def get(self, account_id: str) -> Account | None:
        return self._store.get(account_id)

    def save(self, account: Account) -> None:
        self._store[account.id] = account


if __name__ == "__main__":
    repo = InMemoryAccountRepository()
    repo.save(Account("a-1", "Ada", 100))
    print(repo.get("a-1"))
