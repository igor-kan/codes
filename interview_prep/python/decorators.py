"""Decorators with and without arguments."""
import functools
import time


def timed(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        try:
            return fn(*args, **kwargs)
        finally:
            wrapper.last = time.perf_counter() - start
    return wrapper


def repeat(times: int):
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            return [fn(*args, **kwargs) for _ in range(times)]
        return wrapper
    return decorator


@timed
@repeat(3)
def greet(name: str) -> str:
    return f"hi {name}"


if __name__ == "__main__":
    assert greet("ada") == ["hi ada"] * 3
    assert greet.__name__ == "greet"
    print("ok")
