"""LeetCode 66 - Plus One."""
def plus_one(digits):
    result = list(digits)
    for i in range(len(result) - 1, -1, -1):
        if result[i] < 9:
            result[i] += 1
            return result
        result[i] = 0
    return [1] + result


if __name__ == "__main__":
    assert plus_one([1, 2, 3]) == [1, 2, 4]
    assert plus_one([9, 9]) == [1, 0, 0]
    assert plus_one([4, 3, 2, 1]) == [4, 3, 2, 2]
    print("66 plus one ok")
