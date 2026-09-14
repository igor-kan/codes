import heapq


class MedianFinder:
    def __init__(self) -> None:
        self.low: list[int] = []   # max-heap (negated)
        self.high: list[int] = []  # min-heap

    def add(self, num: int) -> None:
        heapq.heappush(self.low, -num)
        heapq.heappush(self.high, -heapq.heappop(self.low))
        if len(self.high) > len(self.low):
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def median(self) -> float:
        if len(self.low) > len(self.high):
            return float(-self.low[0])
        return (-self.low[0] + self.high[0]) / 2


if __name__ == "__main__":
    finder = MedianFinder()
    for value in [1, 2, 3]:
        finder.add(value)
    assert finder.median() == 2
    print("ok")
