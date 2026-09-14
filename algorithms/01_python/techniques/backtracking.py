"""Backtracking to generate subsets, permutations, and combinations."""

from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    res: List[List[int]] = []

    def backtrack(start: int, current: List[int]):
        res.append(current[:])
        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()

    backtrack(0, [])
    return res


def permutations(nums: List[int]) -> List[List[int]]:
    res: List[List[int]] = []
    used = [False] * len(nums)

    def backtrack(current: List[int]):
        if len(current) == len(nums):
            res.append(current[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            current.append(nums[i])
            backtrack(current)
            current.pop()
            used[i] = False

    backtrack([])
    return res


def combinations(nums: List[int], k: int) -> List[List[int]]:
    res: List[List[int]] = []

    def backtrack(start: int, current: List[int]):
        if len(current) == k:
            res.append(current[:])
            return
        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()

    backtrack(0, [])
    return res


if __name__ == "__main__":
    s = subsets([1, 2, 3])
    assert len(s) == 8
    p = permutations([1, 2, 3])
    assert len(p) == 6
    c = combinations([1, 2, 3, 4], 2)
    assert len(c) == 6
    assert [1, 2] in c
    print("[Python Backtracking] subsets/permutations/combinations verified.")
