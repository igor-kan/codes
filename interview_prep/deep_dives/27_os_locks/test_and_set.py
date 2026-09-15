"""Simulate test-and-set locking with bounded spinning."""
from dataclasses import dataclass


@dataclass
class TestAndSetLock:
    flag: bool = False
    spins: int = 0

    def try_lock(self, max_spins: int = 1000) -> bool:
        local_spins = 0
        while self.flag and local_spins < max_spins:  # test until free or give up
            local_spins += 1
        self.spins += local_spins
        if self.flag:
            return False
        self.flag = True
        return True

    def unlock(self) -> None:
        self.flag = False


if __name__ == "__main__":
    lock = TestAndSetLock()
    assert lock.try_lock() is True
    assert lock.try_lock(max_spins=5) is False   # already held; bounded spin
    assert lock.spins == 5
    lock.unlock()
    assert lock.try_lock() is True
    print("test-and-set ok, spins:", lock.spins)
