"""Write-Ahead Log: append durable records before mutating state."""
from __future__ import annotations

import json
from collections.abc import Iterator
from pathlib import Path


class WriteAheadLog:
    def __init__(self, path: Path) -> None:
        self.path = path

    def append(self, record: dict) -> None:
        with self.path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(record) + "\n")
            handle.flush()
            import os

            os.fsync(handle.fileno())

    def replay(self) -> Iterator[dict]:
        if not self.path.exists():
            return
        with self.path.open(encoding="utf-8") as handle:
            for line in handle:
                yield json.loads(line)


if __name__ == "__main__":
    import tempfile

    wal = WriteAheadLog(Path(tempfile.gettempdir()) / "demo.wal")
    wal.append({"op": "set", "key": "x", "value": 1})
    wal.append({"op": "set", "key": "x", "value": 2})
    state: dict[str, int] = {}
    for record in wal.replay():
        state[record["key"]] = record["value"]
    print(state)
