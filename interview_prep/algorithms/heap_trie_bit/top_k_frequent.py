from collections import Counter
import heapq


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    counts = Counter(nums)
    return heapq.nlargest(k, counts, key=counts.get)


if __name__ == "__main__":
    assert sorted(top_k_frequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
    print("ok")
