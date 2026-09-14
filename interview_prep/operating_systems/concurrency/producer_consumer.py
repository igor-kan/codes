"""Producer/consumer with a queue.Queue (already synchronized)."""
import queue
import threading


def run_producer_consumer(items: int = 100, workers: int = 4) -> list[int]:
    work: queue.Queue = queue.Queue(maxsize=10)
    results: list[int] = []
    result_lock = threading.Lock()
    done = object()

    def producer() -> None:
        for item in range(items):
            work.put(item)
        for _ in range(workers):
            work.put(done)

    def consumer() -> None:
        while True:
            item = work.get()
            if item is done:
                break
            with result_lock:
                results.append(item * 2)

    threads = [threading.Thread(target=consumer) for _ in range(workers)]
    for t in threads:
        t.start()
    producer = threading.Thread(target=producer)
    producer.start()
    producer.join()
    for t in threads:
        t.join()
    return results


if __name__ == "__main__":
    results = run_producer_consumer()
    assert sorted(results) == [i * 2 for i in range(100)]
    print("producer/consumer ok")
