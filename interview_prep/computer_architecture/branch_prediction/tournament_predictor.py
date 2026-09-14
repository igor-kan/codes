"""Tournament predictor choosing between two component predictors."""
from dataclasses import dataclass, field


@dataclass
class TournamentPredictor:
    size: int
    counters: list[int] = field(default_factory=list)
    local: list[int] = field(default_factory=list)
    global_hist: int = 0
    chooser: list[int] = field(default_factory=list)

    def __post_init__(self) -> None:
        self.counters = [1] * self.size
        self.local = [1] * self.size
        self.chooser = [1] * self.size

    def predict(self, pc: int) -> bool:
        index = pc % self.size
        local_pred = self.local[index] >= 1
        global_pred = bin(pc ^ self.global_hist).count("1") % 2 == 0
        return local_pred if self.chooser[index] >= 1 else global_pred

    def update(self, pc: int, taken: bool) -> None:
        index = pc % self.size
        local_pred = self.local[index] >= 1
        self.local[index] = min(2, self.local[index] + 1) if taken else max(0, self.local[index] - 1)
        self.global_hist = ((self.global_hist << 1) | int(taken)) & 0xFF
        if local_pred == taken:
            self.chooser[index] = min(2, self.chooser[index] + 1)
        else:
            self.chooser[index] = max(0, self.chooser[index] - 1)


if __name__ == "__main__":
    predictor = TournamentPredictor(size=32)
    outcomes = [True, True, False, True] * 8
    correct = sum(
        (predictor.predict(0x2000) == taken) + (predictor.update(0x2000, taken) or 1) * 0
        for taken in outcomes
    )
    assert correct > 0
    print("tournament predictor ran")
