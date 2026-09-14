def single_number(nums: list[int]) -> int:
    result = 0
    for n in nums:
        result ^= n
    return result


if __name__ == "__main__":
    assert single_number([4, 1, 2, 1, 2]) == 4
    print("ok")
