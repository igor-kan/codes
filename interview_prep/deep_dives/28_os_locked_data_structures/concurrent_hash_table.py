"""Lock-striped hash table."""
import threading
from dataclasses import dataclass, field


class StripedHashTable:
    def __init__(self, buckets: int = 16) -> None:
        self.locks = [threading.Lock() for _ in range(buckets)]
        self.tables: list[dict[str, int]] = [dict() for _ in range(buckets)]
        self.buckets = buckets

    def _index(self, key: str) -> int:
        return hash(key) % self.buckets

    def put(self, key: str, value: int) -> None:
        index = self._index(key)
        with self.locks[index]:
            self.tables[index][key] = value

    def get(self, key: str) -> int | None:
        index = self._index(key)
        with self.locks[index]:
            return self.tables[index].get(key)

    def size(self) -> int:
        return sum(len(table) for table in self.tables)


if __name__ == "__main__":
    table = StripedHashTable()
    threads = [threading.Thread(target=table.put, args=(f"k{i}", i)) for i in range(200)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    assert table.size() == 200 and table.get("k42") == 42
    print("striped hash table ok")
