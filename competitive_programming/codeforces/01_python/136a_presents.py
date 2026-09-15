"""Codeforces 136A - Presents."""
def presents(permutation):
    result = [0] * len(permutation)
    for index, giver in enumerate(permutation):
        result[giver - 1] = index + 1
    return result


if __name__ == "__main__":
    assert presents([2, 3, 4, 1]) == [4, 1, 2, 3]
    print("136A presents ok")
