"""2-bit saturating counter branch predictor."""
from dataclasses import dataclass, field

STRONGLY_NOT_TAKEN, WEAKLY_NOT_TAKEN, WEAKLY_TAKEN, STRONGLY_TAKEN = 0, 1, 2, 3


@dataclass
class TwoBitPredictor:
    size: int
    counters: list[int] = field(default_factory=list)

    def __post_init__(self) -> None:
        self.counters = [WEAKLY_NOT_TAKEN] * self.size

    def predict(self, pc: int) -> bool:
        return self.counters[pc % self.size] >= WEAKLY_TAKEN

    def update(self, pc: int, taken: bool) -> None:
        index = pc % self.size
        if taken:
            self.counters[index] = min(STRONGLY_TAKEN, self.counters[index] + 1)
        else:
            self.counters[index] = max(STRONGLY_NOT_TAKEN, self.counters[index] - 1)


if __name__ == "__main__":
    predictor = TwoBitPredictor(size=64)
    outcomes = [True] * 8 + [False] * 2
    correct = 0
    for i, taken in enumerate(outcomes):
        pc = 0x1000
        correct += predictor.predict(pc) == taken
        predictor.update(pc, taken)
    assert correct >= len(outcomes) - 3
    print("2-bit predictor accuracy:", correct / len(outcomes))
