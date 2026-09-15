"""Active Record: the object wraps its own row and persistence."""
class ActiveRecord:
    _store: dict[int, dict] = {}
    _next_id = 1

    def __init__(self, **fields) -> None:
        self._fields = fields
        self.id: int | None = None

    def save(self) -> None:
        if self.id is None:
            self.id = ActiveRecord._next_id
            ActiveRecord._next_id += 1
        ActiveRecord._store[self.id] = dict(self._fields)

    @classmethod
    def find(cls, record_id: int):
        return cls(**cls._store[record_id]) if record_id in cls._store else None

    def __getitem__(self, key):
        return self._fields[key]


if __name__ == "__main__":
    record = ActiveRecord(name="Ada")
    record.save()
    loaded = ActiveRecord.find(record.id)
    assert loaded is not None and loaded["name"] == "Ada"
    print("active record ok")
