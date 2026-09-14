import bisect


def lis(nums: list[int]) -> int:
    tails: list[int] = []
    for n in nums:
        i = bisect.bisect_left(tails, n)
        if i == len(tails):
            tails.append(n)
        else:
            tails[i] = n
    return len(tails)


if __name__ == "__main__":
    assert lis([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    print("ok")
