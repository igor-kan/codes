"""Event Sourcing: state as an ordered log of events."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Event:
    kind: str
    amount: int = 0


class Account:
    def __init__(self) -> None:
        self.balance = 0
        self.version = 0

    def apply(self, event: Event) -> None:
        if event.kind == "deposited":
            self.balance += event.amount
        elif event.kind == "withdrawn":
            self.balance -= event.amount
        self.version += 1


def replay(events: list[Event]) -> Account:
    account = Account()
    for event in events:
        account.apply(event)
    return account


if __name__ == "__main__":
    events = [Event("deposited", 100), Event("withdrawn", 30), Event("deposited", 5)]
    account = replay(events)
    assert account.balance == 75 and account.version == 3
    print("event sourcing ok")
