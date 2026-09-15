"""Ticket lock: FIFO fairness via fetch-and-add."""
import threading


class TicketLock:
    def __init__(self) -> None:
        self.next_ticket = 0
        self.now_serving = 0
        self._guard = threading.Lock()

    def lock(self) -> int:
        with self._guard:
            ticket = self.next_ticket
            self.next_ticket += 1
        while True:
            with self._guard:
                if self.now_serving == ticket:
                    return ticket

    def unlock(self) -> None:
        with self._guard:
            self.now_serving += 1


if __name__ == "__main__":
    lock = TicketLock()
    order: list[int] = []

    def worker(index: int) -> None:
        lock.lock()
        order.append(index)
        lock.unlock()

    threads = [threading.Thread(target=worker, args=(i,)) for i in range(5)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    assert order == sorted(order)
    print("ticket lock order:", order)
