"""Wavelet tree for range k-th smallest queries (0-indexed k)."""
class WaveletTree:
    def __init__(self, values: list[int], lo: int | None = None, hi: int | None = None) -> None:
        self.lo = lo if lo is not None else min(values)
        self.hi = hi if hi is not None else max(values)
        self.left: "WaveletTree | None" = None
        self.right: "WaveletTree | None" = None
        self.prefix: list[int] = [0]
        if not values or self.lo == self.hi:
            return
        mid = (self.lo + self.hi) // 2
        lows, highs = [], []
        for value in values:
            if value <= mid:
                lows.append(value)
            else:
                highs.append(value)
            self.prefix.append(self.prefix[-1] + (1 if value <= mid else 0))
        self.left = WaveletTree(lows, self.lo, mid)
        self.right = WaveletTree(highs, mid + 1, self.hi)

    def kth(self, left: int, right: int, k: int) -> int | None:
        if left > right:
            return None
        if self.left is None or self.right is None:
            return self.lo
        left_before = self.prefix[left]
        left_count = self.prefix[right + 1] - left_before
        if k < left_count:
            return self.left.kth(left_before, left_before + left_count - 1, k)
        right_before = left - left_before
        return self.right.kth(right_before, right_before + (right - left + 1 - left_count) - 1, k - left_count)


if __name__ == "__main__":
    tree = WaveletTree([3, 1, 4, 1, 5, 9, 2, 6])
    assert tree.kth(0, 7, 0) == 1
    assert tree.kth(0, 7, 7) == 9
    assert tree.kth(1, 4, 1) == 1
    assert tree.kth(1, 4, 3) == 5
    print("wavelet tree ok")
