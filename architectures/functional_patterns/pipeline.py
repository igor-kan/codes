"""Composing transformations left-to-right."""
from functools import reduce


def pipe(*functions):
    return lambda value: reduce(lambda acc, fn: fn(acc), functions, value)


if __name__ == "__main__":
    process = pipe(str.strip, str.lower, lambda s: s.replace(" ", "-"))
    assert process("  Hello World  ") == "hello-world"
    print("pipeline ok")
