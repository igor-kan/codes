"""Rich comparisons, hashing, callability."""
from functools import total_ordering


@total_ordering
class Version:
    def __init__(self, major: int, minor: int) -> None:
        self.parts = (major, minor)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Version) and self.parts == other.parts

    def __lt__(self, other: "Version") -> bool:
        return self.parts < other.parts

    def __hash__(self) -> int:
        return hash(self.parts)

    def __str__(self) -> str:
        return ".".join(map(str, self.parts))


class Adder:
    def __call__(self, a: int, b: int) -> int:
        return a + b


if __name__ == "__main__":
    assert Version(1, 2) < Version(1, 10)
    assert len({Version(1, 0), Version(1, 0)}) == 1
    assert Adder()(2, 3) == 5
    print("ok")
