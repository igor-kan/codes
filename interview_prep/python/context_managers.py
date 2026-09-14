"""Context managers via classes and contextlib."""
import contextlib
import time


class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc, tb) -> bool:
        self.elapsed = time.perf_counter() - self.start
        return exc_type is None or issubclass(exc_type, ValueError)


@contextlib.contextmanager
def transaction(log: list):
    log.append("begin")
    try:
        yield log
    except Exception:
        log.append("rollback")
        raise
    else:
        log.append("commit")


if __name__ == "__main__":
    events: list[str] = []
    with transaction(events) as txn:
        txn.append("write")
    assert events == ["begin", "write", "commit"]

    with Timer() as timer:
        pass
    assert timer.elapsed >= 0
    print("ok")
