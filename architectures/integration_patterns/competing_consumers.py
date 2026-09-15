"""Competing Consumers: multiple workers drain one queue."""
import queue
import threading


def process(items: list[int], workers: int = 3) -> list[int]:
    work: queue.Queue = queue.Queue()
    for item in items:
        work.put(item)
    results: list[int] = []
    lock = threading.Lock()

    def worker() -> None:
        while True:
            try:
                item = work.get_nowait()
            except queue.Empty:
                return
            with lock:
                results.append(item * 2)
            work.task_done()

    threads = [threading.Thread(target=worker) for _ in range(workers)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    return sorted(results)


if __name__ == "__main__":
    assert process(list(range(10))) == [i * 2 for i in range(10)]
    print("competing consumers ok")
