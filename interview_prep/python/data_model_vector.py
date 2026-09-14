"""A Vector type exercising the Python data model."""
import math


class Vector:
    def __init__(self, *components: float) -> None:
        self._components = tuple(float(c) for c in components)

    def __repr__(self) -> str:
        return f"Vector({', '.join(map(str, self._components))})"

    def __len__(self) -> int:
        return len(self._components)

    def __getitem__(self, index: int) -> float:
        return self._components[index]

    def __iter__(self):
        return iter(self._components)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(*(a + b for a, b in zip(self, other)))

    def __mul__(self, scalar: float) -> "Vector":
        return Vector(*(c * scalar for c in self))

    def __abs__(self) -> float:
        return math.hypot(*self._components)

    def __bool__(self) -> bool:
        return bool(abs(self))


if __name__ == "__main__":
    v = Vector(3, 4)
    assert len(v) == 2 and abs(v) == 5.0
    assert repr(v * 2) == "Vector(6.0, 8.0)"
    print("ok")
