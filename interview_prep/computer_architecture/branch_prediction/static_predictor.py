"""Static branch predictors: always-not-taken and BTFN."""
from dataclasses import dataclass


@dataclass
class Branch:
    address: int
    target: int
    taken: bool


def always_not_taken(branches: list[Branch]) -> tuple[int, int]:
    correct = sum(1 for b in branches if not b.taken)
    return correct, len(branches)


def backward_taken_forward_not(branches: list[Branch]) -> tuple[int, int]:
    correct = 0
    for b in branches:
        prediction = b.target < b.address  # backward branch predicted taken
        correct += prediction == b.taken
    return correct, len(branches)


if __name__ == "__main__":
    branches = [
        Branch(0x100, 0x080, True),    # loop back -> backward taken
        Branch(0x200, 0x300, False),   # forward, not taken
        Branch(0x400, 0x380, True),
    ]
    assert always_not_taken(branches)[0] == 1
    assert backward_taken_forward_not(branches)[0] == 3
    print("static predictors ok")
