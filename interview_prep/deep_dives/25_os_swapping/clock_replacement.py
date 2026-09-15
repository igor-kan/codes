"""Clock (second-chance) replacement approximation of LRU."""
from dataclasses import dataclass, field


@dataclass
class Frame:
    page: int | None = None
    referenced: bool = True


@dataclass
class Clock:
    frames: int
    slots: list[Frame] = field(default_factory=list)
    hand: int = 0
    faults: int = 0

    def __post_init__(self) -> None:
        self.slots = [Frame() for _ in range(self.frames)]

    def access(self, page: int) -> bool:
        for slot in self.slots:
            if slot.page == page:
                slot.referenced = True
                return True
        self.faults += 1
        while True:
            slot = self.slots[self.hand]
            if slot.page is None or not slot.referenced:
                slot.page = page
                slot.referenced = True
                self.hand = (self.hand + 1) % self.frames
                return False
            slot.referenced = False
            self.hand = (self.hand + 1) % self.frames


if __name__ == "__main__":
    clock = Clock(frames=3)
    for page in [1, 2, 3, 4, 1, 2, 5, 1]:
        clock.access(page)
    assert clock.faults > 0
    print("clock faults:", clock.faults)
