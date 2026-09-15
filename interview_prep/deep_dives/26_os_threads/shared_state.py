"""Shared state via globals, thread-local storage and immutability."""
import threading

counter = 0
lock = threading.Lock()
local = threading.local()


def accumulate(values: list[int]) -> int:
    global counter
    local.total = 0
    for value in values:
        local.total += value
        with lock:
            counter += value
    return local.total


if __name__ == "__main__":
    results: dict[int, int] = {}

    def runner(index: int) -> None:
        results[index] = accumulate(list(range(10)))

    threads = [threading.Thread(target=runner, args=(i,)) for i in range(3)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    assert all(total == 45 for total in results.values())
    assert counter == 3 * 45
    print("shared state ok")
