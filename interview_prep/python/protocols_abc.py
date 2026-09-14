"""Structural typing with Protocol and nominal typing with ABC."""
from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable


class Shape(Protocol):
    def area(self) -> float: ...


@runtime_checkable
class Closeable(Protocol):
    def close(self) -> None: ...


class Circle:
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return 3.14159 * self.radius ** 2


class Repository(ABC):
    @abstractmethod
    def get(self, key: str) -> str: ...


class MemoryRepository(Repository):
    def __init__(self) -> None:
        self.data: dict[str, str] = {}

    def get(self, key: str) -> str:
        return self.data[key]


def summarise(shapes: list[Shape]) -> float:
    return sum(shape.area() for shape in shapes)


if __name__ == "__main__":
    assert summarise([Circle(1), Circle(2)]) > 0
    print("ok")
