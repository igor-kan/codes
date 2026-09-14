"""Dependency Inversion: the domain defines ports, infrastructure implements them."""
from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass


# --- Domain layer ---
@dataclass(frozen=True)
class User:
    id: str
    email: str


class UserRepository(ABC):           # port owned by the domain
    @abstractmethod
    def find_by_email(self, email: str) -> User | None: ...

    @abstractmethod
    def save(self, user: User) -> None: ...


class RegisterUser:
    def __init__(self, repo: UserRepository) -> None:
        self._repo = repo

    def execute(self, email: str) -> User:
        if self._repo.find_by_email(email):
            raise ValueError("email already registered")
        user = User(id="new", email=email)
        self._repo.save(user)
        return user


# --- Infrastructure layer (extends the port) ---
class InMemoryUserRepository(UserRepository):
    def __init__(self) -> None:
        self._users: dict[str, User] = {}

    def find_by_email(self, email: str) -> User | None:
        return next((u for u in self._users.values() if u.email == email), None)

    def save(self, user: User) -> None:
        self._users[user.id] = user


if __name__ == "__main__":
    use_case = RegisterUser(InMemoryUserRepository())
    print(use_case.execute("ada@example.com"))
