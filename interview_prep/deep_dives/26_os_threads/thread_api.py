"""Thread creation, joining and return values."""
import threading


def worker(index: int, results: dict) -> None:
    results[index] = index * index


if __name__ == "__main__":
    results: dict[int, int] = {}
    threads = [threading.Thread(target=worker, args=(i, results)) for i in range(5)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    assert results == {i: i * i for i in range(5)}
    print("thread api ok")
