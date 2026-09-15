"""Fencing tokens prevent stale leaders from mutating state."""
from dataclasses import dataclass


@dataclass
class Storage:
    highest_token: int = 0

    def write(self, token: int, value: str) -> bool:
        if token < self.highest_token:
            return False
        self.highest_token = token
        return True


if __name__ == "__main__":
    storage = Storage()
    assert storage.write(2, "from leader 2")
    assert not storage.write(1, "from stale leader 1")
    print("fencing token ok")
