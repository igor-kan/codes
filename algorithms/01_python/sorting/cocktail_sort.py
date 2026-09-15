"""Cocktail (bidirectional bubble) sort."""
def cocktail_sort(a: list) -> list:
    a = list(a)
    start, end = 0, len(a) - 1
    swapped = True
    while swapped:
        swapped = False
        for i in range(start, end):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True
        if not swapped:
            break
        swapped = False
        end -= 1
        for i in range(end, start, -1):
            if a[i] < a[i - 1]:
                a[i], a[i - 1] = a[i - 1], a[i]
                swapped = True
        start += 1
    return a


if __name__ == "__main__":
    data = [5, 1, 4, 2, 8, 0, 2]
    assert cocktail_sort(data) == sorted(data)
    print("cocktail sort ok")
