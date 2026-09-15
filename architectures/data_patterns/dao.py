"""Data Access Object: isolate persistence from domain logic."""
from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True)
class Record:
    id: int
    name: str


class RecordDao(ABC):
    @abstractmethod
    def find(self, record_id: int) -> Record | None: ...

    @abstractmethod
    def all(self) -> list[Record]: ...


class InMemoryRecordDao(RecordDao):
    def __init__(self) -> None:
        self._rows = {1: Record(1, "Ada"), 2: Record(2, "Grace")}

    def find(self, record_id: int) -> Record | None:
        return self._rows.get(record_id)

    def all(self) -> list[Record]:
        return list(self._rows.values())


if __name__ == "__main__":
    dao = InMemoryRecordDao()
    assert dao.find(2).name == "Grace" and len(dao.all()) == 2
    print("dao ok")
