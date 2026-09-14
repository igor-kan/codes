def rotate(nums: list[int], k: int) -> None:
    n = len(nums)
    k %= n

    def reverse(lo: int, hi: int) -> None:
        while lo < hi:
            nums[lo], nums[hi] = nums[hi], nums[lo]
            lo, hi = lo + 1, hi - 1

    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6, 7]
    rotate(data, 3)
    assert data == [5, 6, 7, 1, 2, 3, 4]
    print("ok")
