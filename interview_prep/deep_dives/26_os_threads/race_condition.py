"""A data race demonstrated with and without a lock."""
import threading


def run_without_lock(iterations: int = 100_000) -> int:
    counter = [0]

    def bump() -> None:
        for _ in range(iterations):
            counter[0] += 1

    threads = [threading.Thread(target=bump) for _ in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return counter[0]


def run_with_lock(iterations: int = 100_000) -> int:
    counter = [0]
    lock = threading.Lock()

    def bump() -> None:
        for _ in range(iterations):
            with lock:
                counter[0] += 1

    threads = [threading.Thread(target=bump) for _ in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return counter[0]


if __name__ == "__main__":
    assert run_with_lock() == 400_000
    print("with lock is always correct:", run_with_lock(1000))
