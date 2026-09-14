import heapq


def find_kth_largest(nums: list[int], k: int) -> int:
    return heapq.nlargest(k, nums)[-1]


if __name__ == "__main__":
    assert find_kth_largest([3, 2, 1, 5, 6, 4], 2) == 5
    print("ok")
