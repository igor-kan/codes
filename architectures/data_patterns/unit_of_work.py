"""Unit of Work: track new/dirty/removed objects and commit atomically."""
from dataclasses import dataclass, field


class UnitOfWork:
    def __init__(self) -> None:
        self.new: list[object] = []
        self.dirty: set[int] = set()
        self.removed: list[object] = []

    def register_new(self, obj: object) -> None:
        self.new.append(obj)

    def register_dirty(self, obj: object) -> None:
        self.dirty.add(id(obj))

    def register_removed(self, obj: object) -> None:
        self.removed.append(obj)

    def commit(self, store: dict) -> dict:
        for obj in self.new:
            store[obj["id"]] = dict(obj)
        for obj_id in self.dirty:
            for obj in self.new + list(store.values()):
                if id(obj) == obj_id and isinstance(obj, dict):
                    store[obj["id"]] = dict(obj)
        for obj in self.removed:
            store.pop(obj["id"], None)
        self.new, self.dirty, self.removed = [], set(), []
        return store


if __name__ == "__main__":
    store: dict = {}
    uow = UnitOfWork()
    user = {"id": 1, "name": "Ada"}
    uow.register_new(user)
    uow.commit(store)
    assert store[1]["name"] == "Ada"
    print("unit of work ok")
