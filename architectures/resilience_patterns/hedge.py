"""Hedged requests: issue a backup request to cut tail latency."""
from concurrent.futures import ThreadPoolExecutor, as_completed


def hedged(fn, replicas: int = 2):
    with ThreadPoolExecutor(max_workers=replicas) as pool:
        futures = [pool.submit(fn, i) for i in range(replicas)]
        for future in as_completed(futures):
            return future.result()
    raise RuntimeError("no replica succeeded")


if __name__ == "__main__":
    assert hedged(lambda i: 10 + i, replicas=3) in (10, 11, 12)
    print("hedge ok")
