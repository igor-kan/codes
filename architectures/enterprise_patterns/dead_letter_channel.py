"""Dead Letter Channel: park messages that repeatedly fail processing."""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class DeadLetterChannel:
    max_attempts: int = 3
    attempts: dict[str, int] = field(default_factory=dict)
    dead_letters: list[dict] = field(default_factory=list)

    def process(self, message: dict, handler) -> bool:
        key = message["id"]
        self.attempts[key] = self.attempts.get(key, 0) + 1
        try:
            handler(message)
            return True
        except Exception:  # noqa: BLE001
            if self.attempts[key] >= self.max_attempts:
                self.dead_letters.append(message)
            return False


if __name__ == "__main__":
    channel = DeadLetterChannel()
    bad = {"id": "m-1", "body": "poison"}
    for _ in range(3):
        channel.process(bad, lambda m: (_ for _ in ()).throw(ValueError("boom")))
    print("dead letters:", channel.dead_letters)
