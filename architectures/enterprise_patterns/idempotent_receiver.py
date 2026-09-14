"""Idempotent Receiver: de-duplicate retried messages using a seen set."""
from __future__ import annotations


class IdempotentReceiver:
    def __init__(self) -> None:
        self._seen: set[str] = set()
        self.processed = 0

    def handle(self, message_id: str, payload: dict) -> bool:
        if message_id in self._seen:
            return False
        self._seen.add(message_id)
        self.processed += 1
        # ... persist the effect keyed by message_id ...
        return True


if __name__ == "__main__":
    receiver = IdempotentReceiver()
    print(receiver.handle("m-1", {"total": 10}))
    print(receiver.handle("m-1", {"total": 10}))
    print("processed:", receiver.processed)
