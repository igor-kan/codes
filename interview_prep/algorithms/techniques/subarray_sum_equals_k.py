from collections import defaultdict


def subarray_sum(nums: list[int], k: int) -> int:
    prefix = 0
    seen: dict[int, int] = defaultdict(int)
    seen[0] = 1
    count = 0
    for n in nums:
        prefix += n
        count += seen[prefix - k]
        seen[prefix] += 1
    return count


if __name__ == "__main__":
    assert subarray_sum([1, 1, 1], 2) == 2
    print("ok")
