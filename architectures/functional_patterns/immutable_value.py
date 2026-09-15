"""Immutable value objects for safe sharing."""
from dataclasses import dataclass, replace


@dataclass(frozen=True, slots=True)
class Point:
    x: float
    y: float

    def translate(self, dx: float, dy: float) -> "Point":
        return replace(self, x=self.x + dx, y=self.y + dy)


if __name__ == "__main__":
    origin = Point(0, 0)
    moved = origin.translate(2, 3)
    assert origin == Point(0, 0) and moved == Point(2, 3)
    assert hash(origin) == hash(Point(0, 0))
    print("immutable value ok")
