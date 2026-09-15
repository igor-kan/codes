"""A CAS-based lock and lock-free counter."""
from dataclasses import dataclass, field
import threading


@dataclass
class CasLock:
    state: int = 0  # 0 free, 1 held
    _guard: threading.Lock = field(default_factory=threading.Lock)

    def compare_and_swap(self, expected: int, new: int) -> bool:
        with self._guard:
            if self.state == expected:
                self.state = new
                return True
            return False

    def lock(self) -> None:
        while not self.compare_and_swap(0, 1):
            pass

    def unlock(self) -> None:
        self.state = 0


if __name__ == "__main__":
    lock = CasLock()
    counter = [0]

    def bump() -> None:
        for _ in range(1000):
            lock.lock()
            counter[0] += 1
            lock.unlock()

    threads = [threading.Thread(target=bump) for _ in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    assert counter[0] == 4000
    print("compare-and-swap lock ok")
