"""Entity: an object defined by identity, not attributes."""
from __future__ import annotations

from dataclasses import dataclass, field
from uuid import UUID, uuid4


@dataclass(eq=False)
class Customer:
    name: str
    id: UUID = field(default_factory=uuid4)

    def rename(self, name: str) -> None:
        if not name.strip():
            raise ValueError("name is required")
        self.name = name

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Customer) and self.id == other.id

    def __hash__(self) -> int:
        return hash(self.id)


if __name__ == "__main__":
    a = Customer("Ada")
    b = Customer("Ada")
    print("same id?", a == b)
    a.rename("Ada Lovelace")
    print(a.name)
