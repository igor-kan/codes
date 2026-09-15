"""Comb sort: shrinking-gap bubble sort."""
def comb_sort(a: list) -> list:
    a = list(a)
    gap = len(a)
    shrink = 1.3
    swapped = True
    while gap > 1 or swapped:
        gap = max(1, int(gap / shrink))
        swapped = False
        for i in range(len(a) - gap):
            if a[i] > a[i + gap]:
                a[i], a[i + gap] = a[i + gap], a[i]
                swapped = True
    return a


if __name__ == "__main__":
    data = [8, 4, 1, 56, 3, -44, 23, 6, 5]
    assert comb_sort(data) == sorted(data)
    print("comb sort ok")
