"""Shell sort with Ciura gap sequence."""


def shell_sort(values: list[int]) -> list[int]:
    result = values[:]
    gaps = [701, 301, 132, 57, 23, 10, 4, 1]
    for gap in gaps:
        for i in range(gap, len(result)):
            temp = result[i]
            j = i
            while j >= gap and result[j - gap] > temp:
                result[j] = result[j - gap]
                j -= gap
            result[j] = temp
    return result


if __name__ == "__main__":
    data = [12, 34, 54, 2, 3]
    assert shell_sort(data) == sorted(data)
    print(shell_sort(data))
