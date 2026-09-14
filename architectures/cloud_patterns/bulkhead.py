"""Bulkhead: isolate workloads so one failure cannot exhaust all resources."""
from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor


class Bulkhead:
    def __init__(self, name: str, max_concurrency: int) -> None:
        self.name = name
        self.pool = ThreadPoolExecutor(max_workers=max_concurrency, thread_name_prefix=name)

    def submit(self, fn, *args):
        return self.pool.submit(fn, *args)

    def shutdown(self) -> None:
        self.pool.shutdown(wait=True)


if __name__ == "__main__":
    critical = Bulkhead("critical", 4)
    batch = Bulkhead("batch", 1)
    futures = [critical.submit(lambda n=n: n * n) for n in range(4)]
    print([f.result() for f in futures])
    critical.shutdown()
    batch.shutdown()
