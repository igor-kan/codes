"""Fibonacci search on a sorted array."""
def fibonacci_search(a: list, target: int) -> int:
    fib_m2, fib_m1 = 0, 1
    fib_m = fib_m2 + fib_m1
    while fib_m < len(a):
        fib_m2, fib_m1 = fib_m1, fib_m
        fib_m = fib_m2 + fib_m1
    offset = -1
    while fib_m > 1:
        i = min(offset + fib_m2, len(a) - 1)
        if a[i] < target:
            fib_m, fib_m1, fib_m2 = fib_m1, fib_m2, fib_m1 - fib_m2
            offset = i
        elif a[i] > target:
            fib_m, fib_m1, fib_m2 = fib_m2, fib_m1 - fib_m2, fib_m2 - (fib_m1 - fib_m2)
        else:
            return i
    if fib_m1 and offset + 1 < len(a) and a[offset + 1] == target:
        return offset + 1
    return -1


if __name__ == "__main__":
    arr = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90]
    assert fibonacci_search(arr, 85) == 8
    print("fibonacci search ok")
