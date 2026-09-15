"""Option and Either monads for absence and errors."""
from dataclasses import dataclass
from typing import Callable, Generic, TypeVar

T = TypeVar("T")
U = TypeVar("U")


@dataclass(frozen=True)
class Some(Generic[T]):
    value: T

    def bind(self, fn: Callable[[T], object]) -> object:
        return fn(self.value)


@dataclass(frozen=True)
class Nothing:
    def bind(self, fn: Callable) -> "Nothing":
        return self


@dataclass(frozen=True)
class Ok(Generic[T]):
    value: T

    def bind(self, fn: Callable[[T], object]) -> object:
        return fn(self.value)


@dataclass(frozen=True)
class Err:
    error: str

    def bind(self, fn: Callable) -> "Err":
        return self


def parse(text: str) -> object:
    return Ok(int(text))


if __name__ == "__main__":
    assert parse("42").bind(lambda n: Ok(n + 1)).value == 43
    assert isinstance(Err("bad").bind(lambda n: Ok(n)), Err)
    result = Some(2).bind(lambda n: Some(n * n))
    assert result.value == 4
    assert isinstance(Nothing().bind(lambda n: Some(n)), Nothing)
    print("option/either ok")
