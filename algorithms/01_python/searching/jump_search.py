"""Jump search with step sqrt(n)."""
import math


def jump_search(a: list, target: int) -> int:
    n = len(a)
    step = int(math.sqrt(n)) or 1
    prev = 0
    while prev < n and a[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n)) or 1
        if prev >= n:
            return -1
    while prev < min(step, n) and a[prev] < target:
        prev += 1
    return prev if prev < n and a[prev] == target else -1


if __name__ == "__main__":
    arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    assert jump_search(arr, 13) == 7
    assert jump_search(arr, 4) == -1
    print("jump search ok")
