"""Pancake sort: sort using prefix reversals."""
def flip(a: list, k: int) -> None:
    a[:k] = reversed(a[:k])


def pancake_sort(a: list) -> list:
    a = list(a)
    for size in range(len(a), 1, -1):
        max_index = a.index(max(a[:size]))
        if max_index != size - 1:
            flip(a, max_index + 1)
            flip(a, size)
    return a


if __name__ == "__main__":
    data = [3, 6, 1, 8, 4, 9]
    assert pancake_sort(data) == sorted(data)
    print("pancake sort ok")
