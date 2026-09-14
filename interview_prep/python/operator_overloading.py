"""Operator overloading with explicit semantics."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Matrix:
    rows: tuple[tuple[float, ...], ...]

    def __matmul__(self, other: "Matrix") -> "Matrix":
        n = len(other.rows)
        cols = list(zip(*other.rows))
        return Matrix(tuple(
            tuple(sum(a * b for a, b in zip(row, col)) for col in cols)
            for row in self.rows
        ))

    def __neg__(self) -> "Matrix":
        return Matrix(tuple(tuple(-v for v in row) for row in self.rows))


if __name__ == "__main__":
    a = Matrix(((1, 2), (3, 4)))
    b = Matrix(((0, 1), (1, 0)))
    assert (a @ b).rows == ((2, 1), (4, 3))
    assert (-a).rows == ((-1, -2), (-3, -4))
    print("ok")
