"""Domain Events: record meaningful state changes in the domain."""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Protocol


@dataclass(frozen=True)
class DomainEvent:
    occurred_at: datetime = field(default_factory=lambda: datetime.now(UTC))


@dataclass(frozen=True)
class UserRegistered(DomainEvent):
    user_id: str = ""
    email: str = ""


class EventBus(Protocol):
    def publish(self, event: DomainEvent) -> None: ...


class CollectingBus:
    def __init__(self) -> None:
        self.events: list[DomainEvent] = []

    def publish(self, event: DomainEvent) -> None:
        self.events.append(event)


if __name__ == "__main__":
    bus = CollectingBus()
    bus.publish(UserRegistered(user_id="u1", email="ada@example.com"))
    print(bus.events)
