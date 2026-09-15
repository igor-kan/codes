"""Timeout: bound the time an operation may take."""
import time


class TimeoutError_(Exception):
    pass


def call_with_timeout(fn, timeout_s: float, clock=time.monotonic):
    start = clock()
    result = fn()
    if clock() - start > timeout_s:
        raise TimeoutError_(f"operation exceeded {timeout_s}s")
    return result


if __name__ == "__main__":
    assert call_with_timeout(lambda: 42, 1.0) == 42
    try:
        call_with_timeout(lambda: 0, -1.0)
    except TimeoutError_:
        pass
    else:
        raise AssertionError("expected timeout")
    print("timeout ok")
