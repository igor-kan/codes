"""Randomized selection by recursive partition (CLRS 9.2)."""
import random


def randomized_select(values: list[int], k: int, seed: int = 0) -> int:
    rng = random.Random(seed)
    arr = values[:]

    def select(lo: int, hi: int, k: int) -> int:
        if lo == hi:
            return arr[lo]
        pivot_index = rng.randint(lo, hi)
        arr[pivot_index], arr[hi] = arr[hi], arr[pivot_index]
        pivot = arr[hi]
        i = lo
        for j in range(lo, hi):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[hi] = arr[hi], arr[i]
        if k == i:
            return arr[i]
        if k < i:
            return select(lo, i - 1, k)
        return select(i + 1, hi, k)

    return select(0, len(arr) - 1, k)


if __name__ == "__main__":
    data = [9, 1, 8, 2, 7, 3]
    assert [randomized_select(data, k) for k in range(len(data))] == sorted(data)
    print("randomized quickselect ok")
