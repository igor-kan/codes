"""Stooge sort: a deliberately inefficient recursive sort."""


def stooge_sort(values: list[int], i: int = 0, j: int | None = None) -> list[int]:
    if j is None:
        j = len(values) - 1
    if values[i] > values[j]:
        values[i], values[j] = values[j], values[i]
    if j - i + 1 > 2:
        third = (j - i + 1) // 3
        stooge_sort(values, i, j - third)
        stooge_sort(values, i + third, j)
        stooge_sort(values, i, j - third)
    return values


if __name__ == "__main__":
    data = [5, 1, 4, 2, 8, 3]
    assert stooge_sort(data) == sorted(data)
    print("stooge sort ok")
