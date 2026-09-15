"""LeetCode 35 - Search Insert Position."""
def search_insert(nums, target):
    low, high = 0, len(nums)
    while low < high:
        middle = (low + high) // 2
        if nums[middle] < target:
            low = middle + 1
        else:
            high = middle
    return low


if __name__ == "__main__":
    assert search_insert([1, 3, 5, 6], 5) == 2
    assert search_insert([1, 3, 5, 6], 2) == 1
    assert search_insert([1, 3, 5, 6], 7) == 4
    assert search_insert([1, 3, 5, 6], 0) == 0
    print("35 search insert position ok")
