"""Square-root decomposition for range sums and point updates."""
import math


class SqrtDecomposition:
    def __init__(self, values: list[int]) -> None:
        self.values = list(values)
        self.block = max(1, int(math.isqrt(len(values))))
        self.sums = [
            sum(values[i:i + self.block]) for i in range(0, len(values), self.block)
        ]

    def update(self, index: int, value: int) -> None:
        self.sums[index // self.block] += value - self.values[index]
        self.values[index] = value

    def range_sum(self, left: int, right: int) -> int:
        total = 0
        while left <= right and left % self.block:
            total += self.values[left]
            left += 1
        while left + self.block - 1 <= right:
            total += self.sums[left // self.block]
            left += self.block
        while left <= right:
            total += self.values[left]
            left += 1
        return total


if __name__ == "__main__":
    structure = SqrtDecomposition(list(range(1, 11)))
    assert structure.range_sum(0, 9) == 55
    assert structure.range_sum(2, 5) == 18
    structure.update(4, 100)
    assert structure.range_sum(2, 5) == 113
    print("sqrt decomposition ok")
