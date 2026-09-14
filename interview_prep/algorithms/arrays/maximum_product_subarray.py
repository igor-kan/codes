def max_product(nums: list[int]) -> int:
    best = low = high = nums[0]
    for n in nums[1:]:
        low, high = min(n, low * n, high * n), max(n, low * n, high * n)
        best = max(best, high)
    return best


if __name__ == "__main__":
    assert max_product([2, 3, -2, 4]) == 6
    print("ok")
