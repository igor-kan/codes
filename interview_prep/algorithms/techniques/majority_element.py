def majority_element(nums: list[int]) -> int:
    candidate = count = 0
    for n in nums:
        if count == 0:
            candidate = n
        count += 1 if n == candidate else -1
    return candidate


if __name__ == "__main__":
    assert majority_element([2, 2, 1, 1, 1, 2, 2]) == 2
    print("ok")
