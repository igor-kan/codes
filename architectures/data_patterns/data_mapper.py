"""Data Mapper: transfer data between domain objects and rows."""
from dataclasses import dataclass


@dataclass
class User:
    id: int
    name: str


class UserMapper:
    def to_row(self, user: User) -> dict:
        return {"user_id": user.id, "full_name": user.name}

    def from_row(self, row: dict) -> User:
        return User(id=row["user_id"], name=row["full_name"])


if __name__ == "__main__":
    mapper = UserMapper()
    user = User(1, "Ada")
    row = mapper.to_row(user)
    assert row == {"user_id": 1, "full_name": "Ada"}
    assert mapper.from_row(row) == user
    print("data mapper ok")
