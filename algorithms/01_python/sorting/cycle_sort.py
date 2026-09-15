"""Cycle sort: minimal writes, in place."""
def cycle_sort(a: list) -> list:
    a = list(a)
    for start in range(len(a) - 1):
        item = a[start]
        pos = start
        for i in range(start + 1, len(a)):
            if a[i] < item:
                pos += 1
        if pos == start:
            continue
        while item == a[pos]:
            pos += 1
        a[pos], item = item, a[pos]
        while pos != start:
            pos = start
            for i in range(start + 1, len(a)):
                if a[i] < item:
                    pos += 1
            while item == a[pos]:
                pos += 1
            a[pos], item = item, a[pos]
    return a


if __name__ == "__main__":
    data = [5, 2, 9, 1, 5, 6]
    assert cycle_sort(data) == sorted(data)
    print("cycle sort ok")
